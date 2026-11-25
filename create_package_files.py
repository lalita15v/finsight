
from pathlib import Path

# FinSight source directory
base_dir = Path(__file__).parent / "src" / "finsight"

# Package directories
packages = [
    "",
    "api",
    "core",
    "integrations",
    "reconciliation",
    "exceptions",
    "workflows",
    "models",
    "services",
]

# Create __init__.py in each package
for package in packages:
    package_dir = base_dir / package
    package_dir.mkdir(parents=True, exist_ok=True)

    init_file = package_dir / "__init__.py"
    init_file.touch(exist_ok=True)

    print(f"Created/verified: {init_file}")

print("\nFinSight package files are ready!")



