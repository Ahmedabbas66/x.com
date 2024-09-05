try:
    import cryptography
    import selenium
    import getpass
    print("All modules are installed correctly.")
except ModuleNotFoundError as e:
    print(f"Module not found: {e.name}")
