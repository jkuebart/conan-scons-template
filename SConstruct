# Declare a custom argument, to select a debug or a release build.
AddOption('--debug-build', action='store_true', help='debug build')
is_debug = GetOption('debug_build')

env = Environment()

if not is_debug:
    env.Append(CPPDEFINES=["NDEBUG"])

if "cl" == env["CC"]:
    env.Append(CXXFLAGS=["/EHsc"])

    if is_debug:
        env.Append(CCFLAGS=["/MDd", "/Od"])
    else:
        env.Append(CCFLAGS=["/MD", "/O2"])

else:
    env.Append(CCFLAGS=["-g", "-O0" if is_debug else "-O"])

# Merge flags when building under Conan.
conan = SConscript("SConscript_conan", must_exist=False)
if conan:
    env.MergeFlags(conan["conan"])

libhello = env.Library("hello", ["src/hello.cpp"])

Alias("install", env.Install("/include", Glob("src/*.h")))
Alias("install", env.Install("/lib", libhello))
