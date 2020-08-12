from conans import ConanFile, tools
import os


class HelloConan(ConanFile):
    name = 'Hello'
    version = '1.0'
    license = 'MIT'
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'myproj description'
    exports_sources = "SConstruct", "src/*"
    generators = "scons"

    def scons(self, arguments=None):
        arguments = arguments or []
        debug_opt = \
            ["--debug-build"] if self.settings.build_type == "Debug" else []

        self.run([
            "scons", "--srcdir", self.source_folder,
            *debug_opt, *arguments
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
