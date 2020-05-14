export PyPATH=$HOME/apps/python-3.8.2

export PATH=$PyPATH/bin:$PATH
export LD_LIBRARY_PATH=$PyPATH/lib:$LD_LIBRARY_PATH
export C_INCLUDE_PATH=$PyPATH/Include:$C_INCLUDE_PATH

rm -rf build/

CFLAGS='-Wall -O0 -g' python3 setup.py build
# ln -s -f build/lib.*/*.so .

cd ..
echo `pwd`

ln -s -f */build/lib.*/*.so ./
ls -l *.so
