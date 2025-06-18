# CHANGELOG

## v0.2.0-beta.4 (2025-06-18)

### Build System

- **dep**: Dep update
  ([`c3e77be`](https://github.com/94836615/betok_backend/commit/c3e77be0bdac9e6f68ad5935cead9023d216b55b))

- **dep**: Update
  ([`007c87f`](https://github.com/94836615/betok_backend/commit/007c87f4b6d7ea2571bba3b20bc4662f03711f64))

### Features

- **followers**: Added followers
  ([`1ee93ac`](https://github.com/94836615/betok_backend/commit/1ee93ac712a8f034145caa253b8c97ab99b7cdf8))

## v0.1.1 (2025-03-25)

### Build System

- **dep**: Updated dep
  ([`da48499`](https://github.com/94836615/betok_backend/commit/da484995670793b79c196e849a10da0833af6982))

## v0.2.0-beta.3 (2025-05-21)

### Build System

- **deps**: Updated deps
  ([`eeccb18`](https://github.com/94836615/betok_backend/commit/eeccb18f18a598fb68c989be214c95b51cf75e2d))

### Features

- **likes**: Implemented likes
  ([`4d8c50e`](https://github.com/94836615/betok_backend/commit/4d8c50e5e3b96829ac1f0e7cf99a4f649ad084fb))

- **video-feed/upload**: Refactored and made it possible to see the videos on the front-end. by
  adjusting some code and rebuild the videos function
  ([`32bf6d6`](https://github.com/94836615/betok_backend/commit/32bf6d6f7dba6d2ed117adda4111d18271e55e4d))

- **video-retrieve**: Made it possible to retrieve metadata which in the end will load the video
  ([`615d2d3`](https://github.com/94836615/betok_backend/commit/615d2d36cdd4532d06889737dd009c4d7ae23be9))

### Performance Improvements

- **alembic**: Implemented alembic for db migrations and other stuff
  ([`6b3f12d`](https://github.com/94836615/betok_backend/commit/6b3f12dfc3a019d6ac4c5e2fcbdaec342b164e4d))

### Refactoring

- **metadata-db**: Made it possible that metadata gets stored in a postgrsql db
  ([`989f6fd`](https://github.com/94836615/betok_backend/commit/989f6fda5944aa99c833526fb21ffa35080a99a2))


## v0.2.0-beta.2 (2025-04-01)

### Bug Fixes

- **api**: Fixed the fault where users cant upload their video
  ([`d572cc9`](https://github.com/94836615/betok_backend/commit/d572cc92eeba4244cf0f72d479cee6fffd0137bf))

### Build System

- **deps**: Updated deps
  ([`6110d6c`](https://github.com/94836615/betok_backend/commit/6110d6cc4334d9d5942997fd085fe791e2453e31))

- **deps/config**: Updated deps and adjusted the makefile
  ([`665638f`](https://github.com/94836615/betok_backend/commit/665638fd1ad82c857f9e4b737831f31c3a2feccb))

- **pyproject**: Removed version file temp
  ([`65faceb`](https://github.com/94836615/betok_backend/commit/65faceb110061a85a7be8ab285472a6ca92aa660))

### Refactoring

- **cors**: Cors changes
  ([`56d452c`](https://github.com/94836615/betok_backend/commit/56d452c9294b512c09b432e8ce8cfd1d4c3b9545))

- **video_message**: Adjusted the return message of the endpoint
  ([`800a30a`](https://github.com/94836615/betok_backend/commit/800a30ae68505dceb067393465ddc6d036553d36))


## v0.2.0-beta.1 (2025-03-28)

### Build System

- **pyproject**: Fixed version_variable
  ([`4ffb0d6`](https://github.com/94836615/betok_backend/commit/4ffb0d66998fe7daa8c1c627387471dd141752b4))

### Code Style

- **video-upload**: Fixed a typo
  ([`bbf2e2d`](https://github.com/94836615/betok_backend/commit/bbf2e2d31cac326f50c79a426615ea964922e100))

### Features

- **vid-proc**: Made it possible to upload a video in to the blob storage, also implemented logger
  and did other small adjustments
  ([`d888ca9`](https://github.com/94836615/betok_backend/commit/d888ca9c51191bc24e036cb2493cc7f7d6aef394))

### Performance Improvements

- **logger**: Adjusted logger usage code
  ([`8e10c39`](https://github.com/94836615/betok_backend/commit/8e10c39b199df0fe3b61db1ab064c4c191697e4d))

### Refactoring

- **general_action**: Made new files, renamed it and update deps in prep for feature implementation
  ([`a8d5850`](https://github.com/94836615/betok_backend/commit/a8d585020f5d75357d9b41bd723b87dfc28b7896))

New deps were added, implemented cors and video router and other small adjustments like new files
  and renamed some

- **schema**: Implemented a video schema for video validation
  ([`e75c33c`](https://github.com/94836615/betok_backend/commit/e75c33ca58b55aeb5ffdcc54d76a570652b1ff38))


## v0.1.1-beta.1 (2025-03-25)

### Bug Fixes

- **pipeline**: Pipeline fix
  ([`acc6998`](https://github.com/94836615/betok_backend/commit/acc6998e904708c80d81affbe87608ab8e649ccf))

- **workflow**: Small bug fix versioning
  ([`1eed8b4`](https://github.com/94836615/betok_backend/commit/1eed8b47879c51c00ab074f4ddd2a3532162dcc9))

### Continuous Integration

- **versioning**: Fix in versioning workflow
  ([`f9194ff`](https://github.com/94836615/betok_backend/commit/f9194ff465f47566ea94eeb83768fd225fa165d1))

- **versioning**: Fixed final versioning with version command
  ([`ba10345`](https://github.com/94836615/betok_backend/commit/ba10345e01aa490046d77e1f624f82bfde6ce2b8))

- **versioning**: Typo, deleted publish and added version
  ([`b8a2524`](https://github.com/94836615/betok_backend/commit/b8a25246a32abc11cbb4dc49e2ffa817d92f031c))


## v0.1.0 (2025-03-25)

### Bug Fixes

- **test-upload**: Added a test upload fix
  ([`87cbf8e`](https://github.com/94836615/betok_backend/commit/87cbf8ecca569faf4f819d29238db76174733867))

### Build System

- **deps**: Added a folder structure and update deps
  ([`eecb495`](https://github.com/94836615/betok_backend/commit/eecb4950b5ab0759591b8c3b1c3a51029a0f8da7))

- **deps**: Updated deps
  ([`e9c718e`](https://github.com/94836615/betok_backend/commit/e9c718e1aeed0477c023268f73722b837633aad1))

- **deps**: Updated deps
  ([`6b2e92e`](https://github.com/94836615/betok_backend/commit/6b2e92e103fb3f3335551990be235e3b123a207e))

- **deps**: Updated folder structure and update deps
  ([`881ba3e`](https://github.com/94836615/betok_backend/commit/881ba3e7b5708070627b616debec1978628fedeb))

- **docker**: Changed docker ports
  ([`153169d`](https://github.com/94836615/betok_backend/commit/153169d1bfdf1f7afc1b1f9d34b97264a92c465a))

- **docker**: Changed ip to 0.0.0.0 instead of 127.0.0.1
  ([`70ae05e`](https://github.com/94836615/betok_backend/commit/70ae05eb671ae1b6d0b13f04382db146c634a8c8))

- **docker**: Implemented docker
  ([`3d9776b`](https://github.com/94836615/betok_backend/commit/3d9776b1bbbe62497f65e58703836bc94420823a))

- **fastapi**: Implemented fastapi with a main python file
  ([`bf9649f`](https://github.com/94836615/betok_backend/commit/bf9649f62930ff3caf184d4f6f32ee7a88aa685e))

- **gitignore**: Added a gitignore file
  ([`96cc67c`](https://github.com/94836615/betok_backend/commit/96cc67cdc1251bec5d0cc358bd4226726986e225))

- **gitignore**: Adjusted the gitignore file
  ([`c7edd96`](https://github.com/94836615/betok_backend/commit/c7edd965d5e436ff59d929c4fe941d901eb1f4ca))

- **gitignore**: Updated gitignore with adding python compatibility
  ([`0f01c18`](https://github.com/94836615/betok_backend/commit/0f01c18470050f8f065430890a7c2b13d67be083))

- **makefile**: Added a makefile to type in self-made commands
  ([`c00d055`](https://github.com/94836615/betok_backend/commit/c00d055bfe3ae51588435131fdd27885e3b5ff67))

- **poetry**: Added commitzen to the project
  ([`febb00f`](https://github.com/94836615/betok_backend/commit/febb00ff7f1c76b0b70f15007896d9b02618ac28))

- **poetry**: Adjusted poetry files
  ([`0a8b66b`](https://github.com/94836615/betok_backend/commit/0a8b66b7c585d2cb62eda46142514b4d1f1a6e07))

- **pyproject**: Adjusted pyproject file
  ([`6639056`](https://github.com/94836615/betok_backend/commit/66390561321e1d749aa1a1c58bb0f9d2c6cc7acc))

- **pyproject**: Adjusted the version number for a quickfix
  ([`f1871cf`](https://github.com/94836615/betok_backend/commit/f1871cf5f23cb7c6052c4f9c014205cafb8b73a3))

- **pyproject**: Updated pyproject so it updates the version at tool.poetry
  ([`462f2a3`](https://github.com/94836615/betok_backend/commit/462f2a37ffea98142c8574cae44fa9862175e5a0))

### Code Style

- **main**: Added captial to "world"
  ([`3c74ba8`](https://github.com/94836615/betok_backend/commit/3c74ba8354627f33c92a833e42f313e560b625c2))

### Continuous Integration

- **versioning**: Added a versioning pipeline
  ([`d8a75c1`](https://github.com/94836615/betok_backend/commit/d8a75c15c48ba20abeeca6ba6a8ec1d409309f4b))

### Documentation

- **readme**: Added a readme file
  ([`632066a`](https://github.com/94836615/betok_backend/commit/632066af9ddf9e59a9a86b752cd4fbb155d56ee3))

### Refactoring

- **docker**: Removed useless comments
  ([`0d6c571`](https://github.com/94836615/betok_backend/commit/0d6c571992f373080d5240b15b729b1fc20f0922))
