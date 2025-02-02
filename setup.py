from setuptools import setup, find_packages

setup(
    name='tracer',
    version='0.1',
    packages = ['tracer'],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        tracer-train=tracer.train:cli
        tracer-sim=tracer.simulate:cli
        tracer-eval=tracer.evaluate:cli
        tracer-decode=tracer.train:decode_cli
    ''',
)