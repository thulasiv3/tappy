from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'perception'
object_detection_root = "perception.detection"


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "model"), glob("model/*.*")),
        (os.path.join("share", package_name, "launch"), glob("launch/*")),
    ],
    install_requires=[
        'setuptools',
        'numpy',
        'scipy',
        'opencv-python',
    ],
    zip_safe=True,
    maintainer='Tappy Team',
    maintainer_email='adharsh.kandula@gmail.com',
    description='Code for autonomous key detection and processing for Tappy',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f"key_detector = {object_detection_root}.key_detector_new:main",
            f"mock_baselink = {object_detection_root}.mock_baselink:main",
            f"fake_key_detector = {package_name}.fake_key_detector:main",
            f"aruco_detector = {object_detection_root}.aruco_detector:main",
        ],
    },
)
