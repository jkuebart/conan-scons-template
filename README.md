# Conan SCons template

A template for a [Conan package manager][1] recipe, that uses [SCons][2] as its build tool instead of CMake.
It supports MSVC 2017 Pro and GCC, with a release and a debug build type.

Inside the root directory, just run

    conan create .
    conan create -s build_type=Debug .
    conan create -o Hello:shared=True .
    conan create -o Hello:shared=True -s build_type=Debug .

to test the four possible configurations.

[1]: https://github.com/lasote/conan
[2]: https://bitbucket.org/scons/scons
