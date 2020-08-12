# Declare a custom argument, to select a debug or a release build.
AddOption('--debug-build', action='store_true', help='debug build')
is_debug = GetOption('debug_build')

# Declare an option for a shared library of a specific version.
AddOption('--shlibversion', action='store', help='build shared library')
shlibversion = GetOption('shlibversion')

env = Environment()

if not is_debug:
    env.Append(CPPDEFINES=["NDEBUG"])

if "cl" == env["CC"]:
    env.Append(CXXFLAGS=["/EHsc"])

    if is_debug:
        env.Append(CCFLAGS=["/MDd", "/Od"])
    else:
        env.Append(CCFLAGS=["/MD", "/O2"])

    if shlibversion:
        env.Append(CPPDEFINES=["LIBHELLO_DLL"])

else:
    env.Append(CCFLAGS=["-g", "-O0" if is_debug else "-O"])

# On Darwin, let clients find the library via rpath.
if "darwin" == env["PLATFORM"]:
    env.Append(SHLINKFLAGS=["-Wl,-install_name", "-Wl,@rpath/$TARGET"])

# Merge flags when building under Conan.
conan = SConscript("SConscript_conan", must_exist=False)
if conan:
    env.MergeFlags(conan["conan"])

if shlibversion:
    libhello = env.SharedLibrary("hello", ["src/hello.cpp"], SHLIBVERSION=shlibversion)
    Alias("install", env.InstallVersionedLib("/lib", libhello))

else:
    libhello = env.Library("hello", ["src/hello.cpp"])
    Alias("install", env.Install("/lib", libhello))

Alias("install", env.Install("/include", Glob("src/*.h")))
