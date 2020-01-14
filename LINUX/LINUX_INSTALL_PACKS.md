# PROBLEMAS AO TENTAR ATUALIZAR O LINUX

Options To Fix sub-process /usr/bin/dpkg returned an error code (1)

# SOLUÇÕES

Fonte: https://phoenixnap.com/kb/fix-sub-process-usr-bin-dpkg-returned-error-code-1

Method 1: Reconfigure dpkg Database
If your package database has become corrupted, reconfiguring can repair it.

Enter the following command:

sudo dpkg ––configure –a
This command reconfigures packages that have been unpacked but not necessarily installed. An interruption at the wrong time can cause this database to become corrupt. This is especially helpful if you were running an installation and the process was interrupted.

Method 2: Force-install the Software
If Method 1 did not work, you can attempt to fix the dependencies in the package installer.

Enter the following:

sudo apt-get install –f
The –f option means fix-broken. It repairs any broken dependencies in your package manager. Broken dependencies occur when a download is interrupted, or there is a problem with the cached download.

Note: Dependencies are other software packages that are required by the software you are installing. A package manager helps keep track of dependencies for you.

Method 3: Remove Bad Software Package
If you know which software caused the errors on your system, you can remove it.

Enter the command and package_name with the name of the software that is causing the problem:

sudo apt-get remove ––purge package_name
The ––purge option directs the system to remove config files in addition to uninstalling. This helps get rid of all traces of the offending software.

Method 4: Clean out Unused Software Packages
If an old, outdated, or unused package is causing the problem, you can solve the problem by removing unused software packages.

Enter the following command in the terminal:

sudo apt autoremove
Note: Avoid the next 2 options unless all other methods have failed.

Method 5: Remove Post Files
If you know the name of the package that is causing problems, you can delete the files manually. The installation files are usually located in the /var/lib/dpkg/info file.

Type in the following command and replace package_name with the name of the broken software.:

sudo ls –l /var/lib/dpkg/info | grep –i package_name
This will generate a list of all references to the software you installed.

You can then remove them by entering:

sudo mv /var/lib/dpkg/info/package_name.* /tmp
This command moves the files to the /tmp directory, where they cannot affect your package manager.

Next, update the package manager:

sudo apt-get update
After which you can install the broken software again.

Method 6: Overwrite package file
If you know the name of the package that is causing a problem, you can also force an overwrite.

Use the following command and replace full_name_of_package with the actual package name:

sudo dpkg –i ––force–overwrite /var/cache/apt/archives/full_name_of_package
Note: If you do not know the actual name of the package, you can search for it with the command:

ls /var/cache/apt/archies/*package_name*
 

Replace package_name with the name of your software. This should return any instances of that package name. Note the exact filename, and type it into the previous command.

Conclusion
Ultimately, the dpkg error message indicates that there is a problem with the package installer, most likely caused by an interrupted installation or a corrupted database.

By following these steps, you should have fixed the dpkg error message and have a working package installer.