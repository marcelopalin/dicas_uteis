# INSTALANDO Climate Data Operator (CDO) com NetCDF, GRIB2 e HDF5 no UBUNTU 18+

Referências:

https://code.mpimet.mpg.de/projects/cdo/wiki#Installation-and-Supported-Platforms

https://docs.geoserver.org/latest/en/user/extensions/netcdf-out/nc4.html

http://www.studytrails.com/blog/install-climate-data-operator-cdo-with-netcdf-grib2-and-hdf5-support/

https://www2.nrel.colostate.edu/projects/irc/public/Documents/Software/netCDF/cpp4/html/page_parallel.html

Instale: [GRADS WGRIB2](GRADS_e_WGRIB2.md)


Crie o diretório **cdo-install** em **opt**

$ cd /opt
$ sudo mkdir cdo-install

# BAIXE OS PACOTES

Vá na sua pasta de downloads:

```
$ cd ~/Downloads
$ wget https://www.ece.uvic.ca/~frodo/jasper/software/jasper-2.0.14.tar.gz

$ wget https://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-cxx4-4.3.1.tar.gz

$ wget https://www.zlib.net/zlib-1.2.11.tar.gz

$ wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/hdf5-1.8.13.tar.gz


```

