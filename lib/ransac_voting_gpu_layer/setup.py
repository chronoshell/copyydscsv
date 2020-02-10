from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='ransac_voting',
    ext_modules=[
        CUDAExtension('ransac_voting', [
            '/content/copyydscsv/lib/ransac_voting_gpu_layer/src/ransac_voting.cpp',
            '/content/copyydscsv/lib/ransac_voting_gpu_layer/src/ransac_voting_kernel.cu'
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
