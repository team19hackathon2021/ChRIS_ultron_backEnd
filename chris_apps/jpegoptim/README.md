# jpegoptim

## Build

``` shell
podman build -t jpegoptim .
```

## Check image

``` shell
$ podman images localhost/jpegoptim
REPOSITORY           TAG     IMAGE ID      CREATED        SIZE
localhost/jpegoptim  latest  c42011709ea8  2 minutes ago  5.54 MB
```

## Run

``` shell
podman run --rm -v "$PWD/large.jpeg:/image.jpeg" localhost/jpegoptim:latest /image.jpeg
```

## Usage

``` shell
$ mkdir images

$ cp images/large-original.jpeg images/large.jpeg

$ stat images/large.jpeg
  File: images/large.jpeg
  Size: 6531      	Blocks: 16         IO Block: 4096   regular file
Device: fd02h/64770d	Inode: 462046011   Links: 1
Access: (0777/-rwxrwxrwx)  Uid: ( 1002/  mtulio)   Gid: ( 1030/    devs)
Context: system_u:object_r:container_file_t:s0:c379,c1019
Access: 2021-10-26 15:51:59.147440787 -0300
Modify: 2021-10-26 15:54:45.291054366 -0300
Change: 2021-10-26 15:54:45.291054366 -0300
 Birth: -

$ podman run --rm -v "$PWD/images:/images:Z" localhost/jpegoptim:latest /images/large.jpeg
/images/large.jpeg 200x200 24bit N  [OK] jpegoptim: failed to reset output file group/owner
6531 --> 6019 bytes (7.84%), optimized.

$ stat images/large.jpeg
  File: images/large.jpeg
  Size: 6019      	Blocks: 16         IO Block: 4096   regular file
Device: fd02h/64770d	Inode: 462045987   Links: 1
Access: (0777/-rwxrwxrwx)  Uid: ( 1002/  mtulio)   Gid: ( 1030/    devs)
Context: system_u:object_r:container_file_t:s0:c237,c1005
Access: 2021-10-26 15:55:11.737992604 -0300
Modify: 2021-10-26 15:55:11.737992604 -0300
Change: 2021-10-26 15:55:11.737992604 -0300
 Birth: -
```
