from conans import ConanFile, tools, CMake

class CppCoroConan(ConanFile):
    name = "cppcoro"
    version = "20190416"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True
    scm = {
        "type": "git",
        "url": "git@github.com:lewissbaker/cppcoro.git",
        "revision": "99bb7f80b3e8156ba568e6a113415dce7a38ae08"
    }
    exports_sources = "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
