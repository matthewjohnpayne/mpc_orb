# tests

### local_tests
It is intended that tests that require local MPC functionalities that are likely (at first) to only be available on local machines (e.g. marsden) should be placed in the *local_test" folder.

### nonlocal_tests
It is intended that tests that can be conducted as part of continuous-integration tests on bitbucket/github be placed in the *nonlocal_tests* folder

N.B. The nonlocal_tests *may* require the local_tests to have been produced first to generate intermediate output (esp. the schema files)

