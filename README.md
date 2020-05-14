# Debug c extension of python in eclipse

```
git clone https://github.com/caot/PythonExtensionPatterns.git PythonExtensionPatterns.git
git clone https://github.com/caot/debug_c_code_of_python_in_eclipse.git debug_c_code_of_python.git
```

`ls -lrt` lists the follows two:

```
PythonExtensionPatterns.git
debug_c_code_of_python.git
```

# How to run
debug_c_of_python <path_to_test_sclist.py> test_sclist test

# References
[Effective Techniques for Debugging C & C++](https://www.eclipse.org/community/eclipse_newsletter/2017/april/article2.php)

# build devtoolset-8-gdb
```
wget https://buildlogs.centos.org/c7-devtoolset-8.ppc64le/devtoolset-8-gdb/20190621140321/8.2-3.el7.ppc64le/devtoolset-8-gdb-8.2-3.el7.src.rpm
yum --enablerepo=base-centos-7 install readline-devel ncurses-devel texinfo xz-devel rpm-devel texinfo-tex texlive-collection-latexrecommended mpfr-devel

rpmbuild --rebuild devtoolset-8-gdb-8.2-3.el7.src.rpm # https://wiki.centos.org/HowTos/RebuildSRPM
```

# Building Source RPM as non-root under CentOS*
  Building content as the 'root' user can be a recipe for disaster, whether using the RPM packaging system or plain tarballs. The matter is discussed here in greater detail.
  http://www.owlriver.com/tips/non-root/
  