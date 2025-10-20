FROM quay.io/jupyter/pyspark-notebook
RUN mamba install --yes \
    'polars' && \
    # Remove unused packages and caches (see https://fig.io/manual/mamba/clean)
    mamba clean \
      # Remove index cache, lock files, unused cache packages, and tarballs
      --all \
      # Remove all writable package caches
      --force-pkgs-dirs \
      # Do not ask for confirmation
      --yes
