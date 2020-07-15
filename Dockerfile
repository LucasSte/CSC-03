# start docker image from a python3 image 
FROM python:3.6.9

# create a main folder of the project
RUN mkdir app
WORKDIR /app

# add project code files
ADD main.py Cloud.py DiseaseDetector.py TreeColor.hdf5 src/
RUN mkdir sick_plants_report
RUN mkdir sick_plants_img

# install repo tool
ENV PATH /bin:$PATH
RUN curl https://storage.googleapis.com/git-repo-downloads/repo > /bin/repo
RUN chmod a+x /bin/repo

# install olympe
WORKDIR /app/code/parrot-groundsdk
RUN repo init -u https://github.com/Parrot-Developers/groundsdk-manifest.git
RUN repo sync
RUN ./products/olympe/linux/env/postinst
COPY build/dragon_build/build.py build/dragon_build/build.py
RUN apt-get -y install build-essential yasm cmake libtool libc6 libc6-dev \
    unzip freeglut3-dev libglfw3 libglfw3-dev libsdl2-dev libjson-c-dev \
    libcurl4-gnutls-dev libavahi-client-dev libgles2-mesa-dev
RUN apt-get -y install rsync
RUN apt-get -y install cmake libbluetooth-dev libavahi-client-dev \
    libopencv-dev libswscale-dev libavformat-dev \
    libavcodec-dev libavutil-dev cython python-dev
RUN pip3 install clang
RUN pip3 install -r packages/olympe/requirements.txt
RUN echo "export PYTHONPATH=\$PYTHONPATH:out/olympe-linux/final/usr/lib/python/site-packages/" >> products/olympe/linux/env/setenv
RUN ./build.sh -p olympe-linux -A all final -j


# activate olympe environment and install necessaries python modules
RUN /bin/bash -c "source ./products/olympe/linux/env/shell && pip3 install Keras==2.3.1 && pip3 install tensorflow==1.15.0"

# run code
WORKDIR /app
CMD ["./code/parrot-groundsdk/products/olympe/linux/env/shell", \
        "python3.6", "src/main.py" ]
