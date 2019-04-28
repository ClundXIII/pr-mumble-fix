#pr mumble fix

Download this repo as zip and extract it into the <pr_dir>/mods/pr/bin/PRMurmur folder. Install the ice34-slice_3.4.2-8.2_all.deb package.

Then (for the setup) export the following paths:
```
export LD_LIBRARY_PATH="<pr_dir>/mods/pr/bin/PRMurmur/libs"
export PYTHONPATH="<pr_dir>/mods/pr/bin/PRMurmur/python/Ice/"
```

Then run the initial setup and create channel script as usual. In order to run mumo, post these 2 export lines into the script.

## Important:

*Make sure to have python 2 installed.
*Also you might have to replace the python with "python2" in all those files: `createchannel.sh`, `initialsetup.sh`, `startmumo.sh` to get it working. This will be needed if python3 is present and overwriting your default python.

