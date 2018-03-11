from conans import ConanFile, CMake


class ClippConan(ConanFile):
    name = "clipp"
    version = "20171123"
    license = "MIT"
    url = "https://github.com/muellan/clipp"
    description = "Single-header command parsing library targeted for C++11/14/17"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/muellan/clipp")
        self.run("cd clipp && git checkout c07e8f9")

    def package(self):
        self.copy("clipp.h", dst="include", src="clipp/include")

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.includes = ["include"]
