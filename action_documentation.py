"""Refresh documentation from existing assets without rebuilding parts."""
from working_bearing_documentation import main as generate

def main(**kwargs):
    return generate(**kwargs)

if __name__ == "__main__":
    print(main())
