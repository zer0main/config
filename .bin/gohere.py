#!/usr/bin/env python

""" Install Go into a local directory. """

import argparse
import errno
import hashlib
import logging
import os
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import textwrap
try:
    import urllib2
except:
    # Python 3
    import urllib.request as urllib2


VERSIONS = {
    '1.2.2': 'fbcfe1fe6dfe660cae1c973811c5e2075e3f7b06feea32b4b91c7f0b48352391',
    '1.3': 'eb983e6c5b2b9838f482c5442b1ac1856f610f2b21f3c123b3fedb48ffc35382',
    '1.3.1': 'fdfa148cc12f1e4ea45a5565261bf43d8a2e7d1fad4a16aed592d606223b93a8',
    '1.3.2': '3e7488241c2bf30833629ecbef61e423fe861c6d6d69d2d21a16d2c29eef06fb',
    '1.3.3': '1bb6fde89cfe8b9756a875af55d994cce0994861227b5dc0f268c143d91cd5ff',
    '1.4': '3ae9f67e45a5ca7004b28808da8b1367d328a371d641ddbe636c0fb0ae0ffdae',
    '1.4.1': '66665005fac35ba832ff334977e658f961109d89a7a2358ae7707be0efb16fca',
    '1.4.2': '299a6fd8f8adfdce15bc06bde926e7b252ae8e24dd5b16b7d8791ed79e7b5e9b',
    '1.4.3': '9947fc705b0b841b5938c48b22dc33e9647ec0752bae66e50278df4f23f64959',
    '1.4-bootstrap-20171003': 'f4ff5b5eb3a3cae1c993723f3eab519c5bae18866b5e5f96fe1102f0cb5c3e52',
    '1.5': 'be81abec996d5126c05f2d36facc8e58a94d9183a56f026fc9441401d80062db',
    '1.5.1': 'a889873e98d9a72ae396a9b7dd597c29dcd709cafa9097d9c4ba04cff0ec436b',
    '1.5.2': 'f3ddd624c00461641ce3d3a8d8e3c622392384ca7699e901b370a4eac5987a74',
    '1.5.3': '754e06dab1c31ab168fc9db9e32596734015ea9e24bc44cae7f237f417ce4efe',
    '1.5.4': '002acabce7ddc140d0d55891f9d4fcfbdd806b9332fb8b110c91bc91afb0bc93',
    '1.6': 'a96cce8ce43a9bf9b2a4c7d470bc7ee0cb00410da815980681c8353218dcf146',
    '1.6.1': '1d4b53cdee51b2298afcf50926a7fa44b286f0bf24ff8323ce690a66daa7193f',
    '1.6.2': '787b0b750d037016a30c6ed05a8a70a91b2e9db4bd9b1a2453aa502a63f1bccc',
    '1.6.3': '6326aeed5f86cf18f16d6dc831405614f855e2d416a91fd3fdc334f772345b00',
    '1.6.4': '8796cc48217b59595832aa9de6db45f58706dae68c9c7fbbd78c9fdbe3cd9032',
    '1.7': '72680c16ba0891fcf2ccf46d0f809e4ecf47bbf889f5d884ccb54c5e9a17e1c0',
    '1.7.1': '2b843f133b81b7995f26d0cb64bbdbb9d0704b90c44df45f844d28881ad442d3',
    '1.7.3': '79430a0027a09b0b3ad57e214c4c1acfdd7af290961dd08d322818895af1ef44',
    '1.7.4': '4c189111e9ba651a2bb3ee868aa881fab36b2f2da3409e80885ca758a6b614cc',
    '1.7.5': '4e834513a2079f8cbbd357502cccaac9507fd00a1efe672375798858ff291815',
    '1.7.6': '1a67a4e688673fdff7ba41e73482b0e59ac5bd0f7acf703bc6d50cc775c5baba',
    '1.8': '406865f587b44be7092f206d73fc1de252600b79b3cacc587b74b5ef5c623596',
    '1.8.1': '33daf4c03f86120fdfdc66bddf6bfff4661c7ca11c5da473e537f4d69b470e57',
    '1.8.2': 'e10401faaa8ae29dbe87349c1814b07b1903d453f822215d7b274bbc335cbf79',
    '1.8.3': '5f5dea2447e7dcfdc50fa6b94c512e58bfba5673c039259fd843f68829d99fa6',
    '1.8.4': 'abf1b2e5ae2a4845f3d2eac00c7382ff209e2c132dc35b7ce753da9b4f52e59f',
    '1.8.5': '4949fd1a5a4954eb54dd208f2f412e720e23f32c91203116bed0387cf5d0ff2d',
    '1.8.6': 'efc1221d3ae033c69e149801eff1d9872e214832a89f089fc5beb7a9fd98d9fb',
    '1.8.7': '5911e751807eebbc1980dad4305ef5492b96d6cd720bf93cbcefa86e1c195f9e',
    '1.9': 'a4ab229028ed167ba1986825751463605264e44868362ca8e7accc8be057e993',
    '1.9.1': 'a84afc9dc7d64fe0fa84d4d735e2ece23831a22117b50dafc75c1484f1cb550e',
    '1.9.2': '665f184bf8ac89986cfd5a4460736976f60b57df6b320ad71ad4cef53bb143dc',
    '1.9.3': '4e3d0ad6e91e02efa77d54e86c8b9e34fbe1cbc2935b6d38784dca93331c47ae',
    '1.9.4': '0573a8df33168977185aa44173305e5a0450f55213600e94541604b75d46dc06',
    '1.9.5': 'f1c2bb7f32bbd8fa7a19cc1608e0d06582df32ff5f0340967d83fb0017c49fbc',
    '1.9.6': '36f4059be658f7f07091e27fe04bb9e97a0c4836eb446e4c5bac3c90ff9e5828',
    '1.9.7': '582814fa45e8ecb0859a208e517b48aa0ad951e3b36c7fff203d834e0ef27722',
    '1.10': 'f3de49289405fda5fd1483a8fe6bd2fa5469e005fd567df64485c4fa000c7f24',
    '1.10.1': '589449ff6c3ccbff1d391d4e7ab5bb5d5643a5a41a04c99315e55c16bbf73ddc',
    '1.10.2': '6264609c6b9cd8ed8e02ca84605d727ce1898d74efa79841660b2e3e985a98bd',
    '1.10.3': '567b1cc66c9704d1c019c50bef946272e911ec6baf244310f87f4e678be155f2',
    '1.10.4': '6fe44965ed453cd968a81988523e9b0e794d3a478f91fd7983c28763d52d5781',
    '1.11': 'afc1e12f5fe49a471e3aae7d906c73e9d5b1fdd36d52d72652dde8f6250152fb',
}
BOOTSTRAP_VERSION = '1.4-bootstrap-20171003'
MIN_VERSION_BUILT_WITH_GO = '1.5'
RELOCATION_TYPE_42_VERSIONS = ('1.4.1', '1.4.2', '1.4.3')
MIN_VERSION_WITHOUT_INCLUDE = '1.5'

# cmd/link: support new 386/amd64 relocations
# It is needed to fix build on Debian 8 Stretch.
# See https://github.com/golang/go/issues/13896
# Backport https://github.com/golang/go/commit/914db9f060b1fd3eb1f74d48f3b

RELOCATION_TYPE_42_PATCH = r'''
--- src/cmd/6l/asm.c
+++ src/cmd/6l/asm.c
@@ -117,6 +117,8 @@ adddynrel(LSym *s, Reloc *r)
 		}
 		return;
 	
+	case 256 + R_X86_64_REX_GOTPCRELX:
+	case 256 + R_X86_64_GOTPCRELX:
 	case 256 + R_X86_64_GOTPCREL:
 		if(targ->type != SDYNIMPORT) {
 			// have symbol
--- src/cmd/8l/asm.c
+++ src/cmd/8l/asm.c
@@ -115,6 +115,7 @@ adddynrel(LSym *s, Reloc *r)
 		return;		
 	
 	case 256 + R_386_GOT32:
+	case 256 + R_386_GOT32X:
 		if(targ->type != SDYNIMPORT) {
 			// have symbol
 			if(r->off >= 2 && s->p[r->off-2] == 0x8b) {
--- src/cmd/ld/elf.h
+++ src/cmd/ld/elf.h
@@ -502,8 +502,23 @@ typedef struct {
 #define	R_X86_64_DTPOFF32 21	/* Offset in TLS block */
 #define	R_X86_64_GOTTPOFF 22	/* PC relative offset to IE GOT entry */
 #define	R_X86_64_TPOFF32 23	/* Offset in static TLS block */
-
-#define	R_X86_64_COUNT	24	/* Count of defined relocation types. */
+#define R_X86_64_PC64           24
+#define R_X86_64_GOTOFF64       25
+#define R_X86_64_GOTPC32        26
+#define R_X86_64_GOT64          27
+#define R_X86_64_GOTPCREL64     28
+#define R_X86_64_GOTPC64        29
+#define R_X86_64_GOTPLT64       30
+#define R_X86_64_PLTOFF64       31
+#define R_X86_64_SIZE32         32
+#define R_X86_64_SIZE64         33
+#define R_X86_64_GOTPC32_TLSDEC 34
+#define R_X86_64_TLSDESC_CALL   35
+#define R_X86_64_TLSDESC        36
+#define R_X86_64_IRELATIVE      37
+#define R_X86_64_PC32_BND       40
+#define R_X86_64_GOTPCRELX      41
+#define R_X86_64_REX_GOTPCRELX  42
 
 
 #define	R_ALPHA_NONE		0	/* No reloc */
@@ -535,8 +550,6 @@ typedef struct {
 #define	R_ALPHA_JMP_SLOT	26	/* Create PLT entry */
 #define	R_ALPHA_RELATIVE	27	/* Adjust by program base */
 
-#define	R_ALPHA_COUNT		28
-
 
 #define	R_ARM_NONE		0	/* No relocation. */
 #define	R_ARM_PC24		1
@@ -578,8 +591,6 @@ typedef struct {
 #define	R_ARM_RPC24		254
 #define	R_ARM_RBASE		255
 
-#define	R_ARM_COUNT		38	/* Count of defined relocation types. */
-
 
 #define	R_386_NONE	0	/* No relocation. */
 #define	R_386_32	1	/* Add symbol value. */
@@ -612,8 +623,42 @@ typedef struct {
 #define	R_386_TLS_DTPMOD32 35	/* GOT entry containing TLS index */
 #define	R_386_TLS_DTPOFF32 36	/* GOT entry containing TLS offset */
 #define	R_386_TLS_TPOFF32 37	/* GOT entry of -ve static TLS offset */
-
-#define	R_386_COUNT	38	/* Count of defined relocation types. */
+#define R_386_NONE          0
+#define R_386_32            1
+#define R_386_PC32          2
+#define R_386_GOT32         3
+#define R_386_PLT32         4
+#define R_386_COPY          5
+#define R_386_GLOB_DAT      6
+#define R_386_JMP_SLOT      7
+#define R_386_RELATIVE      8
+#define R_386_GOTOFF        9
+#define R_386_GOTPC         10
+#define R_386_TLS_TPOFF     14
+#define R_386_TLS_IE        15
+#define R_386_TLS_GOTIE     16
+#define R_386_TLS_LE        17
+#define R_386_TLS_GD        18
+#define R_386_TLS_LDM       19
+#define R_386_TLS_GD_32     24
+#define R_386_TLS_GD_PUSH   25
+#define R_386_TLS_GD_CALL   26
+#define R_386_TLS_GD_POP    27
+#define R_386_TLS_LDM_32    28
+#define R_386_TLS_LDM_PUSH  29
+#define R_386_TLS_LDM_CALL  30
+#define R_386_TLS_LDM_POP   31
+#define R_386_TLS_LDO_32    32
+#define R_386_TLS_IE_32     33
+#define R_386_TLS_LE_32     34
+#define R_386_TLS_DTPMOD32  35
+#define R_386_TLS_DTPOFF32  36
+#define R_386_TLS_TPOFF32   37
+#define R_386_TLS_GOTDESC   39
+#define R_386_TLS_DESC_CALL 40
+#define R_386_TLS_DESC      41
+#define R_386_IRELATIVE     42
+#define R_386_GOT32X        43
 
 #define	R_PPC_NONE		0	/* No relocation. */
 #define	R_PPC_ADDR32		1
@@ -653,8 +698,6 @@ typedef struct {
 #define	R_PPC_SECTOFF_HI	35
 #define	R_PPC_SECTOFF_HA	36
 
-#define	R_PPC_COUNT		37	/* Count of defined relocation types. */
-
 #define R_PPC_TLS		67
 #define R_PPC_DTPMOD32		68
 #define R_PPC_TPREL16		69
@@ -697,9 +740,6 @@ typedef struct {
 #define	R_PPC_EMB_BIT_FLD	115
 #define	R_PPC_EMB_RELSDA	116
 
-					/* Count of defined relocation types. */
-#define	R_PPC_EMB_COUNT		(R_PPC_EMB_RELSDA - R_PPC_EMB_NADDR32 + 1)
-
 
 #define R_SPARC_NONE		0
 #define R_SPARC_8		1
--- src/cmd/ld/ldelf.c
+++ src/cmd/ld/ldelf.c
@@ -888,12 +888,15 @@ reltype(char *pn, int elftype, uchar *siz)
 	case R('6', R_X86_64_PC32):
 	case R('6', R_X86_64_PLT32):
 	case R('6', R_X86_64_GOTPCREL):
+	case R('6', R_X86_64_GOTPCRELX):
+	case R('6', R_X86_64_REX_GOTPCRELX):
 	case R('8', R_386_32):
 	case R('8', R_386_PC32):
 	case R('8', R_386_GOT32):
 	case R('8', R_386_PLT32):
 	case R('8', R_386_GOTOFF):
 	case R('8', R_386_GOTPC):
+	case R('8', R_386_GOT32X):
 		*siz = 4;
 		break;
 	case R('6', R_X86_64_64):
'''

# Code for patching was copied from hererocks.py commit 8afe7846572440de21e
# https://github.com/mpeterv/hererocks/
# Copyright (c) 2015 - 2016 Peter Melnichenko

class PatchError(Exception):
    pass

class LineScanner(object):
    def __init__(self, lines):
        self.lines = lines
        self.line_number = 1

    def consume_line(self):
        if self.line_number > len(self.lines):
            raise PatchError("source is too short")
        else:
            self.line_number += 1
            return self.lines[self.line_number - 2]

class Hunk(object):
    def __init__(self, start_line, lines):
        self.start_line = start_line
        self.lines = lines

    def add_new_lines(self, old_lines_scanner, new_lines):
        while old_lines_scanner.line_number < self.start_line:
            new_lines.append(old_lines_scanner.consume_line())

        for line in self.lines:
            first_char, rest = line[0], line[1:]

            if first_char in " -":
                # Deleting or copying a line: it must match what's in the diff.
                old_line = old_lines_scanner.consume_line()
                if rest.strip() != old_line.strip():
                    raise PatchError("source is different: %s, %s" % (
                        rest, old_line,
                    ))

            if first_char in " +":
                # Adding or copying a line: add it to the line list.
                new_lines.append(rest)

class FilePatch(object):
    def __init__(self, file_name, lines):
        self.file_name = file_name
        self.hunks = []
        self.new_lines = []
        hunk_lines = None
        start_line = None

        for line in lines:
            first_char = line[0]

            if first_char == "@":
                if start_line is not None:
                    self.hunks.append(Hunk(start_line, hunk_lines))

                match = re.match(r"^@@ \-(\d+)", line)
                start_line = int(match.group(1))
                hunk_lines = []
            else:
                hunk_lines.append(line)

        if start_line is not None:
            self.hunks.append(Hunk(start_line, hunk_lines))

    def prepare_application(self):
        if not os.path.exists(self.file_name):
            raise PatchError("{} doesn't exist".format(self.file_name))

        with open(self.file_name, "r") as handler:
            source = handler.read()

        old_lines = source.splitlines()
        old_lines_scanner = LineScanner(old_lines)

        for hunk in self.hunks:
            hunk.add_new_lines(old_lines_scanner, self.new_lines)

        while old_lines_scanner.line_number <= len(old_lines):
            self.new_lines.append(old_lines_scanner.consume_line())

        self.new_lines.append("")

    def apply(self):
        with open(self.file_name, "wt") as handler:
            handler.write("\n".join(self.new_lines))

class Patch(object):
    def __init__(self, src, root_dir):
        # The first and the last lines are empty.
        lines = textwrap.dedent(src[1:-1]).splitlines()
        lines = [line if line else " " for line in lines]
        self.file_patches = []
        file_lines = None
        file_name = None

        for line in lines:
            if line.startswith('--- '):
                continue
            if line.startswith('+++ '):
                if file_name is not None:
                    self.file_patches.append(FilePatch(file_name, file_lines))
                file_name = os.path.join(root_dir, line[4:])
                file_lines = []
            else:
                file_lines.append(line)

        if file_name is not None:
            self.file_patches.append(FilePatch(file_name, file_lines))

    def apply(self):
        try:
            for file_patch in self.file_patches:
                file_patch.prepare_application()
        except PatchError as e:
            return e.args[0]

        for file_patch in self.file_patches:
            file_patch.apply()

class TempDir(object):
    n = 0
    def __init__(self, echo=None, goroot=None):
        TempDir.n += 1
        self.echoname = 'T%d' % TempDir.n
        self.echodir = '%s/T%d' % (goroot, TempDir.n)
        self.echo = echo

    def __enter__(self):
        if self.echo:
            self.echo('%s="%s"' % (self.echoname, self.echodir))
            self.echo('mkdir -p "$%s"' % self.echoname)
            return '${%s}' % self.echoname
        else:
            self.name = tempfile.mkdtemp()
            return self.name

    def __exit__(self, type, value, traceback):
        if self.echo:
            self.echo('rm -rf "$%s"' % self.echoname)
        else:
            shutil.rmtree(self.name)

def version_tuple(version):
    if version == BOOTSTRAP_VERSION:
        version = "1.4.9"
    return tuple(map(int, (version.split('.'))))

def is_build_with_go(version):
    return version_tuple(version) >= version_tuple(MIN_VERSION_BUILT_WITH_GO)

def get_default_cache():
    # based on hererocks.py
    if os.name == 'nt':
        cache_root = os.getenv('LOCALAPPDATA')
        if cache_root is None:
            cache_root = os.getenv('USERPROFILE')
            if cache_root is None:
                return None
            cache_root = os.path.join(cache_root, 'Local Settings', 'Application Data')
        return os.path.join(cache_root, 'GoHere', 'Cache')
    else:
        home = os.path.expanduser('~')
        if home == '~':
            return None
        else:
            return os.path.join(home, '.cache', 'gohere')

def get_filename(version):
    if 'bootstrap' not in version:
        version += '.src'
    return 'go%s.tar.gz' % version

def get_url(version):
    return 'https://storage.googleapis.com/golang/%s' % get_filename(version)

def download_file(destination, url, echo=None):
    if echo:
        echo('wget -O "%s" "%s"' % (destination, url))
    else:
        with open(destination, 'wb') as d:
            request =  urllib2.urlopen(url)
            shutil.copyfileobj(request, d)
            request.close()
            logging.info('File %s was downloaded from %s', destination, url)

def checksum_of_file(fileobj):
    hasher = hashlib.sha256()
    for chunk in iter(lambda: fileobj.read(1024 ** 2), b''):
        hasher.update(chunk)
    return hasher.hexdigest()

def make_checksum(filepath):
    with open(filepath, 'rb') as f:
        value = checksum_of_file(f)
    logging.info('sha256(%s) = %s', filepath, value)
    return value

def test_checksum(filename, version, echo=None):
    expected_checksum = VERSIONS[version]
    if echo:
        echo('echo "%s  %s" | sha256sum --check --strict -' % (expected_checksum, filename))
    else:
        observed_checksum = make_checksum(filename)
        if expected_checksum == observed_checksum:
            logging.info('Checksum of %s is good', filename)
        else:
            logging.error(
                'Checksum of %s is bad.\nExpected %s,\nobserved %s.',
                filename,
                expected_checksum,
                observed_checksum,
            )
            sys.exit(1)

def unpack_file(parent_of_goroot, archive_name, echo=None):
    if echo:
        echo('tar -C "%s" -xzf "%s"' % (parent_of_goroot, archive_name))
    else:
        with tarfile.open(archive_name, 'r:gz') as archive:
            archive.extractall(parent_of_goroot)
            logging.info('File %s was unpacked to %s', archive_name, parent_of_goroot)

def mkdir_p(path):
    # taken from http://stackoverflow.com/a/600612
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def patch_go(goroot, version, echo=None):
    if version_tuple(version) < version_tuple(MIN_VERSION_WITHOUT_INCLUDE):
        libc_h = os.path.join(goroot, 'include', 'libc.h')
        if echo:
            echo('sed -i.bak -e "s/struct timespec {/struct timespec_disabled_by_gohere {/g" -- "%s"' % libc_h)
        else:
            # https://ci.appveyor.com/project/starius/gohere/build/1.0.5/job/v08nsr6kj98s8xtu
            logging.info('Patching libc.h to fix conflicting timespec (WIN32)')
            with open(libc_h) as f:
                code = f.read()
            code = code.replace(
                'struct timespec {',
                'struct timespec_disabled_by_gohere {',
            )
            with open(libc_h, 'w') as f:
                f.write(code)
    # Fix "shifting a negative signed value is undefined" on clang.
    # See https://travis-ci.org/starius/gohere/jobs/169812907
    if echo:
        echo('find "%s" -name "*.c" -print0 | xargs -0 -I cfile sed -i.bak -e "s/(vlong)~0 << 32/(uvlong)~0 << 32/g" -- cfile' % goroot)
    else:
        for directory, _, files in os.walk(goroot):
            for base in files:
                if base.endswith('.c'):
                    path = os.path.join(directory, base)
                    with open(path) as f:
                        t = f.read()
                    if '(vlong)~0 << 32' in t:
                        logging.info('Patching %s to fix (vlong)~0 << 32', path)
                        t = t.replace('(vlong)~0 << 32', '(uvlong)~0 << 32')
                        with open(path, 'w') as f:
                            f.write(t)
    # Patch Go 1.4 to prevent https://github.com/golang/go/issues/13896
    # The patch is not applicable to Go 1.4 because line numbers shift.
    if version in RELOCATION_TYPE_42_VERSIONS:
        if echo:
            echo('cd "%s" && patch -p0 -u << EOF\n%s\nEOF' % (goroot, RELOCATION_TYPE_42_PATCH))
        else:
            logging.info('Patching to "fix unknown relocation type 42"')
            err = Patch(RELOCATION_TYPE_42_PATCH, goroot).apply()
            if err is not None:
                raise Exception(err)
    # Fix "implicit conversion from 'int' to 'char' changes" errors.
    # https://travis-ci.org/starius/gohere/jobs/323022483#L2346
    if version_tuple(version) < version_tuple(BOOTSTRAP_VERSION):
        dwarf_c = os.path.join(goroot, 'src', 'cmd', 'ld', 'dwarf.c')
        if echo:
            echo('sed -i.bak -e "s/DW_CFA_offset/((char)(DW_CFA_offset))/g" -- "%s"' % dwarf_c)
            echo('sed -i.bak -e "s/DW_OP_call_frame_cfa/((char)(DW_OP_call_frame_cfa))/g" -- "%s"' % dwarf_c)
        else:
            logging.info('Patching dwarf.c to fix implicit conversion errors')
            with open(dwarf_c) as f:
                code = f.read()
            code = code.replace('DW_CFA_offset', '((char)(DW_CFA_offset))')
            code = code.replace('DW_OP_call_frame_cfa', '((char)(DW_OP_call_frame_cfa))')
            with open(dwarf_c, 'w') as f:
                f.write(code)

def build_go(goroot_final, goroot, goroot_bootstrap=None, test=False, echo=None):
    action = 'all' if test else 'make'
    cwd = os.path.join(goroot, 'src')
    if not echo:
        cwd = os.path.abspath(cwd)
    if os.name == 'nt':
        # Otherwise Windows can not find the batch file
        args = [os.path.join(cwd, '%s.bat' % action)]
    else:
        args = ['./%s.bash' % action]
    if echo:
        echo(
            'cd "%s" && GOROOT_FINAL="%s" GOROOT_BOOTSTRAP="%s" %s | grep "Installed Go"' %
            (cwd, goroot_final, goroot_bootstrap or '', ' '.join(args))
        )
    else:
        env = os.environ.copy()
        env['GOROOT_FINAL'] = goroot_final
        if goroot_bootstrap:
            env['GOROOT_BOOTSTRAP'] = goroot_bootstrap
            logging.info('Go bootstrap is %s', goroot_bootstrap)
        logging.info('Building Go in %s', cwd)
        go_process = subprocess.Popen(
            args,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        (stdout_data, stderr_data) = go_process.communicate()
        logging.info('Exit code is %d', go_process.returncode)
        if not isinstance(stdout_data, str):
            stdout_data = stdout_data.decode()
        if not isinstance(stderr_data, str):
            stderr_data = stderr_data.decode()
        if go_process.returncode != 0 or 'Installed Go' not in stdout_data:
            logging.error('Failed to build Go.')
            logging.error('stdout: %s', stdout_data)
            logging.error('stderr: %s', stderr_data)
            sys.exit(1)
        logging.info('Go was built in %s', goroot)

def install_go(goroot_final, goroot, version, echo=None):
    if echo:
        echo('mkdir -p "%s"' % goroot_final)
    else:
        mkdir_p(goroot_final)
    dirs = ['src', 'bin', 'pkg', 'misc']
    if version_tuple(version) < version_tuple(MIN_VERSION_WITHOUT_INCLUDE):
        dirs.append('include')
    if echo:
        dirs2 = ['"%s"' % os.path.join(goroot, d) for d in dirs]
        echo('cp -a %s "%s"' % (' '.join(dirs2), goroot_final))
    else:
        for subdir in dirs:
            src = os.path.join(goroot, subdir)
            dst = os.path.join(goroot_final, subdir)
            shutil.copytree(src, dst)
        logging.info('Go was installed to %s', goroot_final)

def build_race(goroot, echo=None):
    # See https://github.com/golang/go/issues/20512
    go_binary = os.path.join(goroot, 'bin', 'go')
    args = [go_binary, 'install', '-v', '-race', 'std']
    if echo:
        echo(' '.join(args))
    else:
        logging.info('Building Go race in %s', goroot)
        go_process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        (stdout_data, stderr_data) = go_process.communicate()
        logging.info('Exit code is %d', go_process.returncode)
        if not isinstance(stdout_data, str):
            stdout_data = stdout_data.decode()
        if not isinstance(stderr_data, str):
            stderr_data = stderr_data.decode()
        if go_process.returncode != 0:
            logging.error('Failed to build Go.')
            logging.error('stdout: %s', stdout_data)
            logging.error('stderr: %s', stderr_data)
            sys.exit(1)

def get_from_cache_or_download(cache_root, version, tmp_dir, echo=None):
    filename = get_filename(version)
    if not echo and cache_root:
        file_in_cache = os.path.join(cache_root, filename)
        if os.path.isfile(file_in_cache):
            test_checksum(file_in_cache, version)
            logging.info('Reusing file from cache: %s', file_in_cache)
            return file_in_cache
    tmp_name = os.path.join(tmp_dir, filename)
    download_file(tmp_name, get_url(version), echo)
    test_checksum(tmp_name, version, echo)
    if not echo and cache_root:
        mkdir_p(cache_root)
        shutil.move(tmp_name, file_in_cache)
        logging.info('New file was added to cache: %s', file_in_cache)
        return file_in_cache
    else:
        return tmp_name

def make_goroot_bootstrap(cache_root, tmp_dir, echo=None):
    subdir = 'go%s_bootstrap' % BOOTSTRAP_VERSION
    if not echo and cache_root:
        goroot_bootstrap = os.path.join(cache_root, subdir)
        if os.path.exists(goroot_bootstrap):
            logging.info('Reusing bootstrap Go from %s', goroot_bootstrap)
            return goroot_bootstrap
    else:
        goroot_bootstrap = os.path.join(tmp_dir, subdir)
    if not echo:
        logging.info('Building Go bootstrap in %s', goroot_bootstrap)
    gohere(goroot_bootstrap, BOOTSTRAP_VERSION, cache_root, race=False, echo=echo)
    if not echo:
        logging.info('Go bootstrap was built in %s', goroot_bootstrap)
    return goroot_bootstrap

def gohere(
    goroot,
    version,
    cache_root=None,
    test=None,
    race=True,
    echo=None,
    echo_goroot=None,
):
    if echo and not goroot:
        deps = 'bash coreutils wget tar sed gcc make'
        if version in RELOCATION_TYPE_42_VERSIONS:
            deps += ' patch'
        echo('#!/bin/bash')
        echo('# Dependencies: ' + deps)
        echo('set -xue')
        if echo_goroot:
            goroot = echo_goroot
        else:
            echo('if [ -z ${1+x} ]; then echo "Provide future GOROOT as the first argument."; exit 1; fi')
            echo('if [[ "$1" =~ ^/ ]]; then goroot="$1"; else goroot="$PWD/$1"; fi')
            goroot = '${goroot}'
    if not echo:
        goroot = os.path.abspath(goroot)
    if cache_root is None:
        cache_root = get_default_cache()
    if version not in VERSIONS:
        logging.error('Go version %s is unknown. Try --update-versions', version)
        sys.exit(1)
    if not echo and os.path.exists(goroot):
        logging.error('%s already exists. Remove it manually', goroot)
        sys.exit(1)
    goroot_bootstrap = None
    with TempDir(echo, goroot) as tmp_dir:
        if is_build_with_go(version):
            if not echo:
                logging.info('Go bootstrap is needed for Go %s', version)
            goroot_bootstrap = make_goroot_bootstrap(cache_root, tmp_dir, echo)
            if not echo:
                logging.info('Using Go bootstrap in %s', goroot_bootstrap)
        archive = get_from_cache_or_download(cache_root, version, tmp_dir, echo)
        unpack_file(tmp_dir, archive, echo)
        goroot_build = os.path.join(tmp_dir, 'go')
        patch_go(goroot_build, version, echo)
        build_go(goroot, goroot_build, goroot_bootstrap, test, echo)
        install_go(goroot, goroot_build, version, echo)
        if race:
            build_race(goroot, echo)
        if not echo:
            logging.info('Go %s was built and installed to %s', version, goroot)

def find_all_go_versions():
    req = urllib2.urlopen('https://golang.org/dl/')
    html = req.read()
    req.close()
    return set(
        match.group(1)
        for match
        in re.finditer(r'go([0-9.]+).src.tar.gz', html)
    )

def remote_checksum(version):
    logging.info('Getting checksum of Go %s', version)
    req = urllib2.urlopen(get_url(version))
    value = checksum_of_file(req)
    req.close()
    return value

def find_checksums(versions):
    return {
        version: remote_checksum(version)
        for version in versions
    }

def update_versions():
    all_go_versions = find_all_go_versions()
    # parse this file
    this_file = sys.argv[0]
    with open(this_file) as f:
        this_file_content = f.read()
    sep1 = 'VERSIONS = {'
    sep2 = '}'
    (prefix, other) = this_file_content.split(sep1, 1)
    (known_versions_text, suffix) = other.split(sep2, 1)
    known_versions = {
        match.group(1): match.group(2)
        for match
        in re.finditer(r"'([0-9a-z.-]+)': '([0-9a-f]+)'", known_versions_text)
    }
    new_go_versions = set(all_go_versions) - set(known_versions)
    known_versions.update(find_checksums(new_go_versions))
    known_versions = sorted(
        known_versions.items(),
        key=lambda kv: version_tuple(kv[0]),
    )
    versions_text = '\n'.join(
        "    '%s': '%s'," % (version, checksum)
        for (version, checksum)
        in known_versions
    )
    with open(this_file, 'wt') as f:
        f.write(prefix + sep1 + '\n' + versions_text + '\n' + sep2 + suffix)

def printer(x):
    print(x)

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        'goroot',
        type=str,
        help='Root of Go',
        nargs='?',
    )
    group.add_argument(
        '--update-versions',
        action='store_true',
        help='Update list of Go verions instead of normal operation',
    )
    group.add_argument(
        '--echo',
        action='store_true',
        help='Produce shell code instead',
    )
    parser.add_argument(
        '--echo-goroot',
        type=str,
        help='Hardcoded GOROOT for --echo',
    )
    parser.add_argument(
        '--version',
        type=str,
        help='Go version',
        default=max(VERSIONS, key=version_tuple),
    )
    parser.add_argument(
        '--cache',
        type=str,
        help='Cache for downloaded Go sources',
        default=get_default_cache(),
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Enable Go tests (takes several minutes to complete)',
    )
    parser.add_argument(
        '--race',
        type=str,
        choices=['yes', 'no', 'auto'],
        default='auto',
        help='Whether to build std with -race',
    )
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    if args.update_versions:
        update_versions()
        return
    if args.race == 'auto':
        race = (platform.system() != 'Windows')
    elif args.race == 'yes':
        race = True
    elif args.race == 'no':
        race = False
    goroot = args.goroot
    echo = args.echo
    if echo:
        echo = printer
    gohere(
        goroot,
        args.version,
        args.cache,
        args.test,
        race=race,
        echo=echo,
        echo_goroot=args.echo_goroot,
    )

if __name__ == '__main__':
    main()
