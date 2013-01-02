from distutils.core import setup
setup(name="Gaia",
      version="1.0",
      package_dir={"gaia":"src",
                   "ssh":"src"},
      packages=["gaia", "ssh"],
      )
      
