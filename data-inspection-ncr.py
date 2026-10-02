import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

FACILITIES_FILE = "ncr_health_facilities_raw.csv"
POPULATION_FILE = ("ncr_population_annual_pgr_raw.csv")


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ======================================================================
# LOAD DATA
# ======================================================================

# The 'geometry' column is written as c(lon, lat) with no quotes
# Name the columns and rebuild longitude/latitude below
facility_cols = [
    "name", "name.en", "amenity", "building", "healthcare",
    "healthcare.speciality", "operator.type", "capacity.persons",
    "addr.full", "addr.city", "source", "name.fil", "osm_id",
    "osm_type", "lon_raw", "lat_raw",
]
df_fac = pd.read_csv(FACILITIES_FILE, header=None, skiprows=1,
                     names=facility_cols, na_values=["NA"])

# Turn "c(121.00" and "14.55)" to numeric
df_fac["longitude"] = pd.to_numeric(
    df_fac["lon_raw"].str.replace("c(", "", regex=False), errors="coerce")
df_fac["latitude"] = pd.to_numeric(
    df_fac["lat_raw"].str.replace(")", "", regex=False), errors="coerce")
df_fac = df_fac.drop(columns=["lon_raw", "lat_raw"])

df_pop = pd.read_csv(POPULATION_FILE)

section("SAMPLE DATA")
print("\n[Facilities] random sample of 5 rows")
print(df_fac.sample(5, random_state=42))
print("\n[Population] first 12 rows (raw Excel export)")
print(df_pop.head(12))


# ======================================================================
# COLUMNS, DATA TYPES, SHAPE
# ======================================================================
section("COLUMNS, DATA TYPES, SHAPE")

for label, df in [("Facilities", df_fac), ("Population", df_pop)]:
    print(f"\n[{label}] shape: {df.shape} "
          f"({df.shape[0]} rows, {df.shape[1]} columns)")
    print(f"[{label}] NumPy array shape: {df.to_numpy().shape}")
    print(df.dtypes)


# ======================================================================
# LINKING VARIABLES TO RESEARCH QUESTIONS
# ======================================================================
section("VARIABLES LINKED TO MEMBER 1'S QUESTIONS")

# Q1: Which NCR cities fall below standard healthcare capacity benchmarks
#     when measuring the number of health facilities per LGU?
#     -> addr.city (group by LGU), amenity/healthcare (count facilities),
#        population dataset: city name + 2024 total (benchmark ratio)
#
# Q2: How does health facility density compare to population across NCR
#     cities, and which dense LGUs have the highest operational deficit?
#     -> longitude/latitude (density), capacity.persons (capacity),
#        population dataset: 2024 total (compare against facility counts)
#
# Q3: To what extent are LGUs dominated by general/retail services versus
#     specialized centers (hospitals, maternity, diagnostic labs)?
#     -> amenity/healthcare (classify type), healthcare.speciality
#        (specialty detail), addr.city (type mix per LGU)

question_map = pd.DataFrame([
    ("Q1: Cities below facility benchmarks", "Facilities", "addr.city",
     "Group facilities by LGU"),
    ("Q1: Cities below facility benchmarks", "Facilities", "amenity, healthcare",
     "Count facilities by type"),
    ("Q1: Cities below facility benchmarks", "Population", "city name + 2024 population",
     "Population per LGU (benchmark ratio)"),
    ("Q2: Density vs population, biggest deficit", "Facilities", "longitude, latitude",
     "Location / density"),
    ("Q2: Density vs population, biggest deficit", "Facilities", "capacity.persons",
     "Capacity (almost all missing)"),
    ("Q2: Density vs population, biggest deficit", "Population", "2024 population",
     "Compare against facility counts"),
    ("Q3: General vs specialized services", "Facilities", "amenity, healthcare",
     "Label as general/retail or specialized"),
    ("Q3: General vs specialized services", "Facilities", "healthcare.speciality",
     "Extra specialty detail (sparse)"),
    ("Q3: General vs specialized services", "Facilities", "addr.city",
     "Type mix per LGU"),
], columns=["Question", "Dataset", "Variable", "Used for"])

print(question_map.to_string(index=False))


# ======================================================================
# DATA QUALITY ISSUES
# ======================================================================
section("DATA QUALITY: FACILITIES")
n = len(df_fac)

# --- Missing values ---
missing = df_fac.isna().sum()
report = pd.DataFrame({"missing": missing, "pct": (missing / n * 100).round(1)})
print("\nMissing values (highest first):")
print(report.sort_values("missing", ascending=False))

empty_cols = report.index[report["missing"] == n].tolist()
print(f"\nCompletely empty columns: {empty_cols}")

# --- Coordinates ---
no_coords = df_fac[["longitude", "latitude"]].isna().any(axis=1).sum()
outside_ncr = ~(df_fac["longitude"].between(120.9, 121.2)
                & df_fac["latitude"].between(14.35, 14.80))
print(f"\nMissing coordinates: {no_coords} of {n}")
print(f"Coordinates outside the NCR area: {outside_ncr.sum()}")

# --- Capacity ---
cap_missing = df_fac["capacity.persons"].isna().sum()
print(f"\nMissing capacity.persons: {cap_missing} of {n} "
      f"({cap_missing / n:.1%}) -> too sparse for Q2 'operational deficit'")

# --- City names (LGU key) ---
print(f"\nMissing addr.city: {df_fac['addr.city'].isna().sum()} of {n}")
print(f"Distinct addr.city values: {df_fac['addr.city'].nunique()} "
      "(NCR has 17 LGUs -> spelling variants exist)")
print(df_fac["addr.city"].value_counts(dropna=False))

# --- Facility types ---
print("\namenity counts:")
print(df_fac["amenity"].value_counts(dropna=False))
print("\nhealthcare counts (top 10):")
print(df_fac["healthcare"].value_counts(dropna=False).head(10))

# --- Duplicates ---
print(f"\nDuplicate rows: {df_fac.duplicated().sum()}")
print(f"Duplicate osm_id: {df_fac['osm_id'].duplicated().sum()}")


section("DATA QUALITY: POPULATION")

# --- Messy headers ---
unnamed = [c for c in df_pop.columns if "Unnamed" in str(c)]
print(f"\n'Unnamed' columns: {len(unnamed)} of {df_pop.shape[1]}")
print("Real headers are in rows 2-3 (merged Excel cells), not the column names.")

# --- Blank rows ---
print(f"Blank rows: {df_pop.isna().all(axis=1).sum()} of {len(df_pop)}")

# --- Missing population counts ---
# LGU rows sit between the NCR total row and the "Note:" footnote row
pop_cols = df_pop.columns[2:6]                    # 2010, 2015, 2020, 2024 totals
name_col = df_pop.columns[0]
names = df_pop[name_col].astype(str).str.strip()
start = names[names == "NATIONAL CAPITAL REGION (NCR)"].index[0]
end = names[names == "Note:"].index[0]
lgu_rows = df_pop.iloc[start + 1:end].dropna(subset=[name_col])
print(f"\nLGU rows found: {len(lgu_rows)} (NCR should have 17)")
print("Missing population counts in LGU rows:")
print(lgu_rows[pop_cols].isna().sum())
print(f"Blank cells (NumPy count): {int(np.sum(lgu_rows[pop_cols].isna().to_numpy()))}")

# --- Population stored as text ---
pop_col = df_pop.columns[2]                       # 2010 total population
raw = df_pop[pop_col].dropna().astype(str)
print(f"\nPopulation dtype: {df_pop[pop_col].dtype} (should be numeric)")
print(f"Values with commas, e.g. {raw[raw.str.contains(',')].head(3).tolist()}")

numeric = pd.to_numeric(raw.str.replace(",", "", regex=False), errors="coerce")
print(f"After removing commas: {numeric.notna().sum()} numbers, "
      f"{numeric.isna().sum()} still non-numeric")

# --- Rows that are not cities ---
names = df_pop[df_pop.columns[0]].dropna().astype(str).str.strip()
not_city = names[names.str.contains("REGION|CENSUS|POPULATION|Philippine Statistics",
                                    case=False)]
print("\nRows that are titles/totals/footnotes, not cities:")
print(not_city.tolist())