from src.validator import WordDatabaseValidator


validator = WordDatabaseValidator()

validator.validate()

summary = validator.summary()

print()

print("=" * 60)

print("WORD DATABASE VALIDATION")

print("=" * 60)

print()

print("Errors")

print("-" * 20)

if summary["errors"]:

    for error in summary["errors"]:

        print(error)

else:

    print("None")

print()

print("Warnings")

print("-" * 20)

if summary["warnings"]:

    for warning in summary["warnings"]:

        print(warning)

else:

    print("None")

print()

print("Validation Complete")