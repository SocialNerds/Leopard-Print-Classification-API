FROM ubuntu:16.04

# Get user id and group id from arguments
ARG UID
ARG GID

# Create user.
RUN groupadd -r serveruser -g $GID && useradd -ms /bin/bash serveruser -u $UID -g $GID

# Install some packages.
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common python3-software-properties \
    git openjdk-8-jdk curl patch \
    python3-numpy python3-dev python3-pip python3-wheel python3-setuptools && \
    ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip && pip install --upgrade pip
RUN pip install keras_applications keras_preprocessing

# Install bazel.
RUN apt-get install -y --no-install-recommends bash-completion g++ zlib1g-dev unzip && \
    curl -LO "https://github.com/bazelbuild/bazel/releases/download/0.19.2/bazel_0.19.2-linux-x86_64.deb" && \
    dpkg -i bazel_*.deb

# Install TensorFlow.
WORKDIR /
RUN git clone https://github.com/tensorflow/tensorflow && \
    cd tensorflow && ./configure

# Build pip package.
WORKDIR /tensorflow
RUN bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package && \
    bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

# Install pip package.
RUN pip --no-cache-dir install --upgrade /tmp/tensorflow_pkg/tensorflow-*.whl && \
    rm -rf /tmp/tensorflow_pkg && \
    rm -rf /root/.cache

# Install some packages.
RUN pip install h5py tb-nightly scikit-learn pandas Pillow

# Copy keys and create main path.
RUN chown -R serveruser:serveruser /home/serveruser

WORKDIR /home/serveruser/data

EXPOSE 8888 6006 8000

USER serveruser
CMD tail -f /dev/null
