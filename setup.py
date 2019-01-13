import setuptools

setuptools.setup(
        name="cvideo",
        version="0.0.4",
        author="Ross Leitch",
        author_email="ross@end-game.com",
        description="A small wrapper around cv2 to get a video stream in a thread",
        url="https://github.com/balbatross/cv2-video",
        packages=['cvideo'],
        install_requires=[
            'numpy'
        ],
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
)
