set(Deltille_FOUND TRUE)
get_filename_component(DELTILLE_ROOT "${Deltille_DIR}/../../" ABSOLUTE)
set(Deltille_INCLUDE_DIRS "${DELTILLE_ROOT}/include")
set(Deltille_LIBRARY_DIRS "${DELTILLE_ROOT}/lib")
set(Deltille_LIBRARIES "libdeltille.a")
