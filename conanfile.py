from conans import ConanFile, tools
import os


class HelloConan(ConanFile):
    name = 'Hello'
    version = '1.0'
    license = 'MIT'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {"shared": [False, True]}
    default_options = {"shared": False}
    description = 'myproj description'
    exports_sources = "SConstruct", "src/*"
    generators = "scons"

    def scons(self, arguments=None):
        arguments = arguments or []
        debug_opt = \
            ["--debug-build"] if self.settings.build_type == "Debug" else []
        shared_opt = \
            ["--shlibversion={}".format(self.version)] \
            if self.options.shared else []

        self.run([
            "scons", "--srcdir", self.source_folder,
            *debug_opt, *shared_opt, *arguments
        ])

    def build(self):
        # FIXME: Compiler, version, arch are hardcoded, not parametrized
        self.scons()

    def package(self):
        self.scons([
            "install", "--install-sandbox={}".format(self.package_folder)
        ])

    def package_info(self):
        self.cpp_info.libs = ["hello"]

        if self.options.shared:

            # Build paths pointing into our package folder.
            libdirs = [
                os.path.join(self.package_folder, libdir)
                for libdir in self.cpp_info.libdirs
            ]

            if "Windows" == self.settings.os:
                # Add DLLs to PATH on Windews.
                self.env_info.PATH.extend(libdirs)

            else:
                # Use rpath when linking executables on POSIX.
                self.cpp_info.exelinkflags.extend(
                    option
                    for rpath in libdirs
                    for option in ("-Wl,-rpath", "-Wl,{}".format(rpath))
                )
