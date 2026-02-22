#!/usr/bin/env python3
"""
Setup script for building personality_core C extension

Usage:
    python3 setup.py build_ext --inplace
    pip install -e .

Supported Platforms:
    - Linux x64
    - Linux ARM64
    - macOS x64
    - macOS ARM64 (Apple Silicon)
    - Windows x64
"""

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import platform

# 定义C扩展模块
personality_core = Extension(
    'personality_core',
    sources=['personality_core.c'],
    include_dirs=[],
    extra_compile_args=['-O3', '-fPIC'],
    extra_link_args=['-lm']
)

# 编译优化类
class BuildExt(build_ext):
    """Custom build extension class for platform-specific optimizations"""

    def build_extensions(self):
        # 针对不同的编译器设置优化选项
        system = platform.system().lower()

        if system == 'darwin':  # macOS
            # macOS: 支持通用二进制
            for ext in self.extensions:
                # 检查架构
                arch = platform.machine().lower()
                if arch == 'arm64':
                    # Apple Silicon
                    ext.extra_compile_args = ['-O3', '-fPIC', '-arch', 'arm64']
                elif arch == 'x86_64':
                    # Intel Mac
                    ext.extra_compile_args = ['-O3', '-fPIC', '-arch', 'x86_64']
                else:
                    # 通用二进制（同时支持 Intel 和 Apple Silicon）
                    ext.extra_compile_args = ['-O3', '-fPIC', '-arch', 'x86_64', '-arch', 'arm64']

        elif system.startswith('linux'):  # Linux
            # Linux: 使用本地优化
            for ext in self.extensions:
                # 检查是否支持 native 优化
                try:
                    import subprocess
                    result = subprocess.run(
                        ['gcc', '--version'],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        # 使用 native 优化
                        ext.extra_compile_args = ['-O3', '-fPIC', '-march=native', '-mtune=native']
                    else:
                        ext.extra_compile_args = ['-O3', '-fPIC']
                except:
                    ext.extra_compile_args = ['-O3', '-fPIC']

        elif system == 'windows':  # Windows
            # Windows: 使用 MSVC 优化
            for ext in self.extensions:
                ext.extra_compile_args = ['/O2', '/GL']
                ext.extra_link_args = ['/LTCG']
                # 移除 Linux 特定的链接参数
                if '-lm' in ext.extra_link_args:
                    ext.extra_link_args.remove('-lm')

        super().build_extensions()

# 设置包信息
setup(
    name='personality_core',
    version='1.0.0',
    description='Core algorithms for AGI Evolution Model',
    author='AGI Evolution Model Team',
    license='AGPL-3.0',
    ext_modules=[personality_core],
    cmdclass={'build_ext': BuildExt},
    python_requires='>=3.7',
    zip_safe=False,
)