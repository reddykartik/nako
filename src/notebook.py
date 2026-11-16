## {{{ processing raw dataset
import os
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib tk
##

## {{{ constants
SEED = 3
## }}}

## {{{ loading dataset
dirname = os.path.join(os.path.abspath(".."), "data", "raw")
train = pd.read_excel(os.path.join(dirname, "train.xlsx"))
test = pd.read_csv(os.path.join(dirname, "test.csv"))
## }}}

## {{{ missing values, dtypes, shapes and nunique
print("TRAIN DATASET:")
print(train.info())
print("\nTEST DATASET:")
print(test.info())
# TRAIN DATASET:
# <class 'pandas.DataFrame'>
# RangeIndex: 14248 entries, 0 to 14247
# Data columns (total 10 columns):
#  #   Column                      Non-Null Count  Dtype
# ---  ------                      --------------  -----
#  0   __source_file               7950 non-null   str
#  1   cve_ids                     14248 non-null  str
#  2   cwe_ids                     14248 non-null  str
#  3   file_path                   14248 non-null  str
#  4   label                       14248 non-null  int64
#  5   patched_function_source     14147 non-null  str
#  6   predicted_cwe_ids           8830 non-null   str
#  7   repo                        14248 non-null  str
#  8   sha                         14248 non-null  str
#  9   vulnerable_function_source  14193 non-null  str
# dtypes: int64(1), str(9)
# memory usage: 1.1 MB
# None
# 
# TEST DATASET:
# <class 'pandas.DataFrame'>
# RangeIndex: 3563 entries, 0 to 3562
# Data columns (total 10 columns):
#  #   Column                   Non-Null Count  Dtype
# ---  ------                   --------------  -----
#  0   __source_file            1962 non-null   str
#  1   cve_ids                  3563 non-null   str
#  2   cwe_ids                  3563 non-null   str
#  3   file_path                3563 non-null   str
#  4   class                    3563 non-null   int64
#  5   patched_function_source  3545 non-null   str
#  6   predicted_cwe_ids        2204 non-null   str
#  7   repo                     3563 non-null   str
#  8   sha                      3563 non-null   str
#  9   function_code            3563 non-null   str
# dtypes: int64(1), str(9)
# memory usage: 278.5 KB
# None
## }}}

## {{{ viewing dataset samples
print("\nTRAINING SAMPLES:")
print(train.sample(10, random_state=SEED))
# TRAINING SAMPLES:
#                             __source_file  cve_ids  ...                                       sha                         vulnerable_function_source
# 13098  functions_for_airflow_with_cwe.csv  UNKNOWN  ...  af0c83e9bf84e3a0dff782e3a95a9b610d23643d  def _reset_signals():\n    # Uninstall the ric...
# 1945    functions_for_django_with_cwe.csv  UNKNOWN  ...  3b2993ed04f200a89c2d49590131c97c8974e9ac  def get_year(self):\n        """\n        Retu...
# 4176   functions_for_ansible_with_cwe.csv  UNKNOWN  ...  e6190524248ef2747c70e5c04377e78eb63e4d76  def __init__(self, *args, **kwargs):\n        ...
# 4452                                  NaN  UNKNOWN  ...  279f1fae1e8ef08eaff7a3505029fc2cc0508302  def test_async_execute_logging_should_execute_...
# 2005    functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  fc19cde859e92b6e5dcc882a2742e4648e86b4ac  def collect_metrics(self):\n        # Get GPU ...
# 11237                                 NaN  UNKNOWN  ...  64968b7d645e8696492c6455be4692400567f1e3  def initdb():\n    from airflow import models\...
# 9191      functions_for_salt_with_cwe.csv  UNKNOWN  ...  af2a3028d3d18437b5b9f17a96c1f3ebafb7d1db  def install(name=None,\n            refresh=Fa...
# 4179    functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  1ecbd4ac8b16716d2ba08517cec62245d5d20374  def _get_user_defined_estimator(self, X_train,...
# 12366                                 NaN  UNKNOWN  ...  935a9b9d56d1d0ab26ba4493b64851429510d4e3  def test_line_insert_end(self, name):\n       ...
# 4943                                  NaN  UNKNOWN  ...  b8d0dc73c762bedc0a36bb380cded62a7b3ea162  def test_view_with_bad_login(self):\n        "...
# 
# [10 rows x 10 columns]
print("\nTESTING SAMPLES:")
print(test.sample(10, random_state=SEED))
# TESTING SAMPLES:
#                            __source_file  cve_ids  ...                                       sha                                      function_code
# 2395   functions_for_django_with_cwe.csv  UNKNOWN  ...  25c15b17a86fa95b5374b9ef6366450b28a28b7a  def queryset_add(self, request):\n        """\...
# 1273     functions_for_w3af_with_cwe.csv  UNKNOWN  ...  b48bb3ebb41a074f70805cba57bb518768fe7dfb  def _generate_urls(self, url):\n        '''\n ...
# 1601                                 NaN  UNKNOWN  ...  efe163a1fddfd66fa402231906e96733efddf8af  def test_runs_respected_after_clear(self):\n  ...
# 2651                                 NaN  UNKNOWN  ...  b9224ee28f8d1fe669ae9c09738257bcaf0efd19  def test_default_run_context_tags(patch_script...
# 536   functions_for_airflow_with_cwe.csv  UNKNOWN  ...  cb295c351a016c0a10cab07f2a628b865cff3ca3  def execute(self, context: Context) -> Any:\n ...
# 1671  functions_for_ansible_with_cwe.csv  UNKNOWN  ...  7e3916b767e1f02fae67630ce7e81bdf47825282  def get_capabilities(self):\n        """Return...
# 1099   functions_for_sqlmap_with_cwe.csv  UNKNOWN  ...  84ba3d45c1c129a81f6f784b2b04d0d321423ccf  def getChar(idx, charTbl=None, continuousOrder...
# 1737                                 NaN  UNKNOWN  ...  8eec2d93b6e93b8a1107fb3de2acd68d6994d6ec  def render(self, name, value, attrs=None):\n  ...
# 3125                                 NaN  UNKNOWN  ...  66b02cbec463a7179ab6ac2860dd64553afb74d8  def test_add_spans():\n    trace_manager = InM...
# 1567                                 NaN  UNKNOWN  ...  936e7c4755e503cc2a067398e39d485fc8f0984e  def test_handle_failure_no_task(self, Stats_in...
# 
# [10 rows x 10 columns]
print("\nTRAIN UNIQUE VALUES:")
print(train.nunique())
# TRAIN UNIQUE VALUES:
# __source_file                    15
# cve_ids                          22
# cwe_ids                           1
# file_path                      5602
# label                             2
# patched_function_source       14035
# predicted_cwe_ids                41
# repo                             15
# sha                           10772
# vulnerable_function_source    14193
# dtype: int64
print("\nTEST UNIQUE VALUES:")
print(test.nunique())
# TEST UNIQUE VALUES:
# __source_file                15
# cve_ids                      15
# cwe_ids                       1
# file_path                  2225
# class                         2
# patched_function_source    3538
# predicted_cwe_ids            32
# repo                         15
# sha                        3121
# function_code              3563
# dtype: int64
## }}}

## {{{ unique values in dataset
for name, df, target in [
  ("train", train, "label"),
  ("test", test, "class"),
]:
  print(f"\n{name.upper()} DATASET:")
  print("\nClass Distribution:")
  print(df[target].value_counts(normalize=True))
  for column in [
    "__source_file",
    "cve_ids",
    "cwe_ids",
    "file_path",
    "predicted_cwe_ids",
    "repo",
    "sha",
  ]:
    print("\n")
    print(df[column].value_counts())

  print("\n" + "=" * 60)
# TRAIN DATASET:
# 
# Class Distribution:
# label
# 0    0.557973
# 1    0.442027
# Name: proportion, dtype: float64
# 
# 
# __source_file
# functions_for_sqlmap_with_cwe.csv        841
# functions_for_airflow_with_cwe.csv       837
# functions_for_django_with_cwe.csv        832
# functions_for_salt_with_cwe.csv          826
# functions_for_ansible_with_cwe.csv       821
# functions_for_mlflow_with_cwe.csv        813
# functions_for_w3af_with_cwe.csv          719
# functions_for_tornado_with_cwe.csv       512
# functions_for_jupyter_with_cwe.csv       398
# functions_for_bandit_with_cwe.csv        351
# functions_for_volatility_with_cwe.csv    272
# functions_for_paramiko_with_cwe.csv      272
# functions_for_flask_with_cwe.csv         270
# functions_for_requests_with_cwe.csv      141
# functions_for_yaml_with_cwe.csv           45
# Name: count, dtype: int64
# 
# 
# cve_ids
# UNKNOWN           14218
# CVE-2021-20191        3
# CVE-2018-16859        3
# CVE-2024-24680        2
# CVE-2022-34265        2
# CVE-2022-28346        2
# CVE-2020-11652        2
# CVE-2019-6975         2
# CVE-2020-14343        1
# CVE-2024-39330        1
# CVE-2019-14233        1
# CVE-2019-10906        1
# CVE-2021-25281        1
# CVE-2020-24584        1
# CVE-2016-2512         1
# CVE-2021-45115        1
# CVE-2021-44420        1
# CVE-2020-22935        1
# CVE-2024-39329        1
# CVE-2022-23833        1
# CVE-2024-53908        1
# CVE-2022-22936        1
# Name: count, dtype: int64
# 
# 
# cwe_ids
# UNKNOWN    14248
# Name: count, dtype: int64
# 
# 
# file_path
# lib/core/common.py                                 75
# lib/core/agent.py                                  57
# tornado/web.py                                     56
# lib/request/connect.py                             55
# tests/jobs/test_scheduler_job.py                   55
#                                                    ..
# examples/multistep_workflow/train_keras.py          1
# packaging/release.py                                1
# providers/tests/opsgenie/hooks/test_opsgenie.py     1
# airflow/operators/sensors.py                        1
# salt/modules/smbios.py                              1
# Name: count, Length: 5602, dtype: int64
# 
# 
# predicted_cwe_ids
# CWE-703                      3903
# CWE-Unknown                  2181
# CWE-259                       447
# CWE-89                        438
# UNKNOWN                       351
# CWE-79                        277
# CWE-330                       182
# CWE-327                       167
# CWE-605                       151
# CWE-78                        134
# CWE-94                        101
# CWE-20                         88
# CWE-22                         78
# CWE-259, CWE-703               66
# CWE-502                        65
# CWE-94, CWE-330                38
# CWE-295                        22
# CWE-22, CWE-78                 17
# CWE-327, CWE-330               17
# CWE-89, CWE-703                17
# CWE-78, CWE-703                15
# CWE-94, CWE-703                15
# CWE-330, CWE-703               12
# CWE-605, CWE-703                8
# CWE-327, CWE-703                7
# CWE-327, CWE-330, CWE-703       4
# CWE-732                         3
# CWE-94, CWE-327                 3
# CWE-20, CWE-78                  3
# CWE-89, CWE-502                 3
# CWE-89, CWE-259, CWE-703        2
# CWE-89, CWE-259                 2
# CWE-259, CWE-605                2
# CWE-22, CWE-703                 2
# CWE-78, CWE-327, CWE-330        2
# CWE-502, CWE-703                2
# CWE-259, CWE-327                1
# CWE-20, CWE-703                 1
# CWE-20, CWE-78, CWE-327         1
# CWE-295, CWE-327                1
# CWE-330, CWE-502, CWE-703       1
# Name: count, dtype: int64
# 
# 
# repo
# apache/airflow                     2659
# saltstack/salt                     2480
# django/django                      1857
# mlflow/mlflow                      1600
# ansible/ansible                    1307
# sqlmapproject/sqlmap               1066
# andresriancho/w3af                  719
# tornadoweb/tornado                  579
# jupyter/notebook                    431
# pallets/flask                       376
# PyCQA/bandit                        351
# paramiko/paramiko                   303
# volatilityfoundation/volatility     275
# psf/requests                        195
# yaml/pyyaml                          50
# Name: count, dtype: int64
# 
# 
# sha
# 03349014513114f1eaa413a9831b0027e4fbfa67    164
# 8abdd659087504a45cf0d720c018c6ac28b3937f     62
# 9eeeff414d119c7df72b10da3dda8daf000d85ea     55
# cb295c351a016c0a10cab07f2a628b865cff3ca3     42
# df4293473d2fb6e887e31522cab5aff95e201581     40
#                                            ...
# ea55c15367536a5698b40936a9874a51a76e170a      1
# 477ffd848a9dd4326c66cb33907a2d3e010683ed      1
# ef68fd7ee91ffb156a64d06a819206747550a8a2      1
# bda01cf9939e3069837196c6b4e20314ac877d53      1
# a73eb0592c1a0893687b2313976df2d858484cf4      1
# Name: count, Length: 10772, dtype: int64
# 
# ============================================================
# 
# TEST DATASET:
# 
# Class Distribution:
# class
# 0    0.55066
# 1    0.44934
# Name: proportion, dtype: float64
# 
# 
# __source_file
# functions_for_salt_with_cwe.csv          210
# functions_for_django_with_cwe.csv        209
# functions_for_ansible_with_cwe.csv       206
# functions_for_sqlmap_with_cwe.csv        201
# functions_for_mlflow_with_cwe.csv        199
# functions_for_airflow_with_cwe.csv       194
# functions_for_w3af_with_cwe.csv          157
# functions_for_jupyter_with_cwe.csv       121
# functions_for_tornado_with_cwe.csv       111
# functions_for_bandit_with_cwe.csv         89
# functions_for_volatility_with_cwe.csv     89
# functions_for_flask_with_cwe.csv          71
# functions_for_paramiko_with_cwe.csv       64
# functions_for_requests_with_cwe.csv       28
# functions_for_yaml_with_cwe.csv           13
# Name: count, dtype: int64
# 
# 
# cve_ids
# UNKNOWN           3547
# CVE-2020-11652       2
# CVE-2019-6975        2
# CVE-2022-22936       1
# CVE-2024-41989       1
# CVE-2021-45116       1
# CVE-2019-14232       1
# CVE-2018-16859       1
# CVE-2021-25282       1
# CVE-2019-14234       1
# CVE-2024-45230       1
# CVE-2017-12794       1
# CVE-2022-34265       1
# CVE-2021-20191       1
# CVE-2024-37088       1
# Name: count, dtype: int64
# 
# 
# cwe_ids
# UNKNOWN    3563
# Name: count, dtype: int64
# 
# 
# file_path
# lib/core/common.py                                      20
# tests/admin_views/tests.py                              18
# salt/states/archive.py                                  18
# tests/test_requests.py                                  17
# lib/request/connect.py                                  14
#                                                         ..
# lib/ansible/module_utils/network/vyos/facts/facts.py     1
# lib/ansible/modules/system/filesystem.py                 1
# test/units/parsing/test_ajson.py                         1
# salt/modules/ssh.py                                      1
# tests/pytests/unit/client/ssh/test_ssh.py                1
# Name: count, Length: 2225, dtype: int64
# 
# 
# predicted_cwe_ids
# CWE-703                    1008
# CWE-Unknown                 514
# CWE-259                     114
# CWE-89                      101
# UNKNOWN                      89
# CWE-79                       66
# CWE-330                      55
# CWE-327                      42
# CWE-605                      40
# CWE-78                       32
# CWE-94                       25
# CWE-22                       23
# CWE-20                       21
# CWE-259, CWE-703             16
# CWE-502                      12
# CWE-94, CWE-703               6
# CWE-605, CWE-703              5
# CWE-89, CWE-703               4
# CWE-22, CWE-78                4
# CWE-295                       4
# CWE-94, CWE-330               4
# CWE-330, CWE-703              3
# CWE-94, CWE-327               3
# CWE-89, CWE-502               2
# CWE-502, CWE-703              2
# CWE-327, CWE-330              2
# CWE-78, CWE-703               2
# CWE-20, CWE-78, CWE-327       1
# CWE-22, CWE-703               1
# CWE-20, CWE-703               1
# CWE-259, CWE-605              1
# CWE-20, CWE-605               1
# Name: count, dtype: int64
# 
# 
# repo
# apache/airflow                     680
# saltstack/salt                     600
# django/django                      490
# mlflow/mlflow                      379
# ansible/ansible                    340
# sqlmapproject/sqlmap               249
# andresriancho/w3af                 157
# jupyter/notebook                   129
# tornadoweb/tornado                 126
# pallets/flask                       99
# PyCQA/bandit                        89
# volatilityfoundation/volatility     89
# paramiko/paramiko                   71
# psf/requests                        51
# yaml/pyyaml                         14
# Name: count, dtype: int64
# 
# 
# sha
# 03349014513114f1eaa413a9831b0027e4fbfa67    39
# 8abdd659087504a45cf0d720c018c6ac28b3937f    22
# cb295c351a016c0a10cab07f2a628b865cff3ca3    13
# 9043d9dd05a3b9470abeacd9510752999a7479ae    13
# df4293473d2fb6e887e31522cab5aff95e201581    12
#                                             ..
# 3c75808c5c36a7529a93ac1bba9014907fa3e349     1
# 7eb5f532946686c7173c0d95946aa4b49c010cf1     1
# ebce47de7c72a48b7fbd0a67f0b87b906a8801c1     1
# df7338809bb4246ef028258658d049bedaaaca86     1
# cf57e487e263cc4c47f5eaf39916cb5434d720e8     1
# Name: count, Length: 3121, dtype: int64
# 
# ============================================================
## }}}

## {{{ code length
train_vul_length = train["vulnerable_function_source"].dropna().str.len()
train_patch_length = train["patched_function_source"].dropna().str.len()
print(f"\nTRAIN VULNERABLE CODE:\n{train_vul_length}")
print("\nTRAIN VULNERABLE DESCRIBE:\n", train_vul_length.describe())
print(f"\nTRAIN PATCHED CODE:\n{train_patch_length}")
print("\nTRAIN PATCHED DESCRIBE:\n", train_patch_length.describe())
print("\n" + "=" * 60)
test_vul_length = test["function_code"].dropna().str.len()
test_patch_length = test["patched_function_source"].dropna().str.len()
print(f"\nTEST VULNERABLE CODE:\n{test_vul_length}")
print("\nTEST VULNERABLE DESCRIBE:\n", test_vul_length.describe())
print(f"\nTEST PATCHED CODE:\n{test_patch_length}")
print("\nTEST PATCHED DESCRIBE:\n", test_patch_length.describe())
# TRAIN VULNERABLE CODE:
# 0         226
# 1         490
# 2        5555
# 3         734
# 4        2659
#          ...
# 14243    1703
# 14244     195
# 14245    1013
# 14246     978
# 14247     514
# Name: vulnerable_function_source, Length: 14193, dtype: int64
# 
# TRAIN VULNERABLE DESCRIBE:
#  count    14193.000000
# mean      2473.966251
# std       4420.231884
# min         31.000000
# 25%        560.000000
# 50%       1134.000000
# 75%       2415.000000
# max      47979.000000
# Name: vulnerable_function_source, dtype: float64
# 
# TRAIN PATCHED CODE:
# 0         226
# 1         487
# 2        5048
# 3         752
# 4        2660
#          ...
# 14243    1623
# 14244     195
# 14245    1066
# 14246     919
# 14247     482
# Name: patched_function_source, Length: 14147, dtype: int64
# 
# TRAIN PATCHED DESCRIBE:
#  count    14147.000000
# mean      2519.178554
# std       4429.278376
# min         31.000000
# 25%        582.000000
# 50%       1173.000000
# 75%       2496.500000
# max      47984.000000
# Name: patched_function_source, dtype: float64
# 
# ============================================================
# 
# TEST VULNERABLE CODE:
# 0       1216
# 1        293
# 2        621
# 3       7300
# 4       2163
#         ...
# 3558     286
# 3559    1377
# 3560    1628
# 3561    1067
# 3562    2633
# Name: function_code, Length: 3563, dtype: int64
# 
# TEST VULNERABLE DESCRIBE:
#  count      3563.000000
# mean       2667.377210
# std        6153.767939
# min          32.000000
# 25%         555.000000
# 50%        1126.000000
# 75%        2404.500000
# max      137703.000000
# Name: function_code, dtype: float64
# 
# TEST PATCHED CODE:
# 0        1341
# 1         280
# 2         686
# 3       11407
# 4        2175
#         ...
# 3558      435
# 3559     2019
# 3560     2914
# 3561     1164
# 3562     2639
# Name: patched_function_source, Length: 3545, dtype: int64
# 
# TEST PATCHED DESCRIBE:
#  count      3545.000000
# mean       2713.739633
# std        6179.280056
# min          32.000000
# 25%         580.000000
# 50%        1167.000000
# 75%        2481.000000
# max      137707.000000
# Name: patched_function_source, dtype: float64
#
# train histogram
fig, ax = plt.subplots()
ax.hist(train_vul_length, bins=50, alpha=0.5, color="blue", label="vulnerable")
ax.hist(train_patch_length, bins=50, alpha=0.5, color="red", label="patched")
ax.legend()
ax.set_yscale("log")
ax.set_title("Training Histogram")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_histogram.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_histogram.png
# train box plot
fig, ax = plt.subplots()
ax.boxplot(
  [train_vul_length, train_patch_length],
  tick_labels=["vulnerable", "patched"], notch=True)
ax.set_ylabel("Code Size")
ax.set_yscale("log")
ax.set_title("Training Box Plot")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_boxplot.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_boxplot.png
# test histogram
fig, ax = plt.subplots()
ax.hist(test_vul_length, bins=50, alpha=0.5, color="blue", label="vulnerable")
ax.hist(test_patch_length, bins=50, alpha=0.5, color="red", label="patched")
ax.legend()
ax.set_yscale("log")
ax.set_title("Testing Histogram")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_histogram.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_histogram.png
# test box plot
fig, ax = plt.subplots()
ax.boxplot(
  [test_vul_length, test_patch_length],
  tick_labels=["vulnerable", "patched"], notch=True)
ax.set_ylabel("Code Size")
ax.set_yscale("log")
ax.set_title("Testing Box Plot")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_boxplot.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_boxplot.png
# train vulnerable vs patch
train["vulnerable_length"] = train_vul_length
train["patched_length"] = train_patch_length
print("\nTrain Vulnerable vs Patched Length:")
print(train[["vulnerable_length", "patched_length"]].corr())
# Train Vulnerable vs Patched Length:
#                    vulnerable_length  patched_length
# vulnerable_length           1.000000        0.998436
# patched_length              0.998436        1.000000
# training code length visualization
plt.scatter(train["vulnerable_length"], train["patched_length"], alpha=0.3)
plt.xlabel("Vulnerable")
plt.ylabel("Patched")
plt.title("Train Code Length")
plt.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_vul_patch_code_length.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_vul_patch_code_length.png
# test vulnerable vs patch
test["vulnerable_length"] = test_vul_length
test["patched_length"] = test_patch_length
print("\nTest Vulnerable vs Patched Length:")
print(test[["vulnerable_length", "patched_length"]].corr())
# Test Vulnerable vs Patched Length:
#                    vulnerable_length  patched_length
# vulnerable_length           1.000000        0.999561
# patched_length              0.999561        1.000000
plt.scatter(test["vulnerable_length"], test["patched_length"], alpha=0.3)
plt.xlabel("Vulnerable")
plt.ylabel("Patched")
plt.title("Test Code Length")
plt.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_vul_patch_code_length.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_vul_patch_code_length.png
## }}}

## {{{ relationship among columns
for name, df, target in [
  ("train", train, "label"),
  ("test", test, "class"),
]:
  print(f"\n{name.upper()} DATASET:")
  print(f"\nREPOSITORIES PER {target.upper()}:")
  print(df.groupby("repo")[target].agg(["count", "sum", "mean"]))
  print("\n", pd.crosstab(df["repo"], df[target], normalize="index"))
  print(f"\nSOURCE FILE PER {target.upper()}:")
  print(pd.crosstab(df["__source_file"], df[target], normalize="index"))
  print("\n", pd.crosstab(df["__source_file"].isna(), df[target], normalize="index"))
  print(f"\nFILE PATH PER {target.upper()}:")
  print(pd.crosstab(df["file_path"], df[target], normalize="index"))
  pattern = r"(?:^|/)(?:test[^/]*|[^/]*test[^/]*)\.py$"
  is_test = df["file_path"].str.contains(
    pattern,
    case=False,
    regex=True,
    na=False,
  )
  print("\n", pd.crosstab(
    is_test,
    df[target],
    normalize="index",
    margins=True,
  ))
  print("\nTesting:\n", df.loc[is_test, ["file_path", target]].sample(10, random_state=SEED))
  print("\nProduction:\n", df.loc[~is_test, ["file_path", target]].sample(10, random_state=SEED))
  print("\n" + "=" * 60)
# 
# TRAIN DATASET:
# 
# REPOSITORIES PER LABEL:
#                                  count   sum      mean
# repo
# PyCQA/bandit                       351     0  0.000000
# andresriancho/w3af                 719     0  0.000000
# ansible/ansible                   1307   486  0.371844
# apache/airflow                    2659  1822  0.685220
# django/django                     1857  1025  0.551966
# jupyter/notebook                   431    33  0.076566
# mlflow/mlflow                     1600   787  0.491875
# pallets/flask                      376   106  0.281915
# paramiko/paramiko                  303    31  0.102310
# psf/requests                       195    54  0.276923
# saltstack/salt                    2480  1654  0.666935
# sqlmapproject/sqlmap              1066   225  0.211069
# tornadoweb/tornado                 579    67  0.115717
# volatilityfoundation/volatility    275     3  0.010909
# yaml/pyyaml                         50     5  0.100000
# 
#  label                                   0         1
# repo
# PyCQA/bandit                     1.000000  0.000000
# andresriancho/w3af               1.000000  0.000000
# ansible/ansible                  0.628156  0.371844
# apache/airflow                   0.314780  0.685220
# django/django                    0.448034  0.551966
# jupyter/notebook                 0.923434  0.076566
# mlflow/mlflow                    0.508125  0.491875
# pallets/flask                    0.718085  0.281915
# paramiko/paramiko                0.897690  0.102310
# psf/requests                     0.723077  0.276923
# saltstack/salt                   0.333065  0.666935
# sqlmapproject/sqlmap             0.788931  0.211069
# tornadoweb/tornado               0.884283  0.115717
# volatilityfoundation/volatility  0.989091  0.010909
# yaml/pyyaml                      0.900000  0.100000
# 
# SOURCE FILE PER LABEL:
# label                                    0
# __source_file
# functions_for_airflow_with_cwe.csv     1.0
# functions_for_ansible_with_cwe.csv     1.0
# functions_for_bandit_with_cwe.csv      1.0
# functions_for_django_with_cwe.csv      1.0
# functions_for_flask_with_cwe.csv       1.0
# functions_for_jupyter_with_cwe.csv     1.0
# functions_for_mlflow_with_cwe.csv      1.0
# functions_for_paramiko_with_cwe.csv    1.0
# functions_for_requests_with_cwe.csv    1.0
# functions_for_salt_with_cwe.csv        1.0
# functions_for_sqlmap_with_cwe.csv      1.0
# functions_for_tornado_with_cwe.csv     1.0
# functions_for_volatility_with_cwe.csv  1.0
# functions_for_w3af_with_cwe.csv        1.0
# functions_for_yaml_with_cwe.csv        1.0
# 
#  label            0    1
# __source_file
# False          1.0  0.0
# True           0.0  1.0
# 
# FILE PATH PER LABEL:
# label                                                 0    1
# file_path
# IPython/frontend/html/notebook/handlers.py          1.0  0.0
# IPython/frontend/html/notebook/kernelmanager.py     1.0  0.0
# IPython/frontend/html/notebook/nbmanager.py         1.0  0.0
# IPython/frontend/html/notebook/notebook.py          1.0  0.0
# IPython/frontend/html/notebook/notebook/handler...  1.0  0.0
# ...                                                 ...  ...
# waf/virusdie.py                                     1.0  0.0
# waf/wallarm.py                                      1.0  0.0
# waf/watchguard.py                                   1.0  0.0
# waf/webknight.py                                    1.0  0.0
# waf/zenedge.py                                      1.0  0.0
# 
# [5602 rows x 2 columns]
# 
#  label             0         1
# file_path
# False      0.722570  0.277430
# True       0.279917  0.720083
# All        0.557973  0.442027
# 
# Testing:
#                                                 file_path  label
# 1760   airflow-core/tests/unit/api_fastapi/common/db/...      1
# 1138                         tornado/test/ioloop_test.py      0
# 2139                     tests/model_fields/test_uuid.py      0
# 12079         django/contrib/gis/gdal/tests/test_geom.py      0
# 2995   w3af/core/controllers/chrome/tests/test_instru...      0
# 2753               tests/tracking/test_model_registry.py      1
# 8614      tests/forms_tests/tests/test_error_messages.py      1
# 4656   tests/store/artifact/test_databricks_artifact_...      1
# 86                                     tests/test_cli.py      1
# 5211                       chart/tests/test_pgbouncer.py      1
# 
# Production:
#                                                 file_path  label
# 8839                                    flask/helpers.py      0
# 12448                         volatility/win32/rawreg.py      0
# 2725                                  bandit/cli/main.py      0
# 7237              w3af/core/data/context/context/html.py      0
# 9756              notebook/services/sessions/handlers.py      0
# 2949                                django/utils/html.py      1
# 5373                            notebook/nbextensions.py      1
# 726                 lib/ansible/plugins/strategy/free.py      0
# 7797   airflow/contrib/operators/gcp_bigtable_operato...      0
# 1461              airflow/utils/log/file_task_handler.py      0
# 
# ============================================================
# 
# TEST DATASET:
# 
# REPOSITORIES PER CLASS:
#                                  count  sum      mean
# repo
# PyCQA/bandit                        89    0  0.000000
# andresriancho/w3af                 157    0  0.000000
# ansible/ansible                    340  134  0.394118
# apache/airflow                     680  486  0.714706
# django/django                      490  281  0.573469
# jupyter/notebook                   129    8  0.062016
# mlflow/mlflow                      379  180  0.474934
# pallets/flask                       99   28  0.282828
# paramiko/paramiko                   71    7  0.098592
# psf/requests                        51   23  0.450980
# saltstack/salt                     600  390  0.650000
# sqlmapproject/sqlmap               249   48  0.192771
# tornadoweb/tornado                 126   15  0.119048
# volatilityfoundation/volatility     89    0  0.000000
# yaml/pyyaml                         14    1  0.071429
# 
#  class                                   0         1
# repo
# PyCQA/bandit                     1.000000  0.000000
# andresriancho/w3af               1.000000  0.000000
# ansible/ansible                  0.605882  0.394118
# apache/airflow                   0.285294  0.714706
# django/django                    0.426531  0.573469
# jupyter/notebook                 0.937984  0.062016
# mlflow/mlflow                    0.525066  0.474934
# pallets/flask                    0.717172  0.282828
# paramiko/paramiko                0.901408  0.098592
# psf/requests                     0.549020  0.450980
# saltstack/salt                   0.350000  0.650000
# sqlmapproject/sqlmap             0.807229  0.192771
# tornadoweb/tornado               0.880952  0.119048
# volatilityfoundation/volatility  1.000000  0.000000
# yaml/pyyaml                      0.928571  0.071429
# 
# SOURCE FILE PER CLASS:
# class                                    0
# __source_file
# functions_for_airflow_with_cwe.csv     1.0
# functions_for_ansible_with_cwe.csv     1.0
# functions_for_bandit_with_cwe.csv      1.0
# functions_for_django_with_cwe.csv      1.0
# functions_for_flask_with_cwe.csv       1.0
# functions_for_jupyter_with_cwe.csv     1.0
# functions_for_mlflow_with_cwe.csv      1.0
# functions_for_paramiko_with_cwe.csv    1.0
# functions_for_requests_with_cwe.csv    1.0
# functions_for_salt_with_cwe.csv        1.0
# functions_for_sqlmap_with_cwe.csv      1.0
# functions_for_tornado_with_cwe.csv     1.0
# functions_for_volatility_with_cwe.csv  1.0
# functions_for_w3af_with_cwe.csv        1.0
# functions_for_yaml_with_cwe.csv        1.0
# 
#  class            0    1
# __source_file
# False          1.0  0.0
# True           0.0  1.0
# 
# FILE PATH PER CLASS:
# class                                              0    1
# file_path
# IPython/frontend/html/notebook/filenbmanager.py  1.0  0.0
# IPython/frontend/html/notebook/handlers.py       1.0  0.0
# IPython/html/allow76.py                          1.0  0.0
# IPython/html/base/handlers.py                    1.0  0.0
# IPython/html/base/zmqhandlers.py                 1.0  0.0
# ...                                              ...  ...
# waf/siteguard.py                                 1.0  0.0
# waf/sonicwall.py                                 1.0  0.0
# waf/urlmaster.py                                 1.0  0.0
# waf/webknight.py                                 1.0  0.0
# waf/wordfence.py                                 1.0  0.0
# 
# [2225 rows x 2 columns]
# 
#  class             0         1
# file_path
# False      0.714350  0.285650
# True       0.279104  0.720896
# All        0.550660  0.449340
# 
# Testing:
#                                                file_path  class
# 1995  tests/api_fastapi/core_api/routes/public/test_...      1
# 1713           tests/ti_deps/deps/test_dagrun_id_dep.py      0
# 1669               test/units/playbook/test_taggable.py      0
# 2210  test/units/modules/network/f5/test_bigip_gtm_p...      1
# 3391                   tests/tracking/test_log_image.py      1
# 2314  airflow-core/tests/unit/api_fastapi/core_api/r...      1
# 1300  tests/providers/amazon/aws/operators/test_glue.py      1
# 1986    tests/cli/commands/test_internal_api_command.py      1
# 3486         tests/regressiontests/admin_views/tests.py      1
# 3546                 tests/unit/templates/jinja_test.py      1
# 
# Production:
#                                         file_path  class
# 1994             lib/ansible/playbook/helpers.py      1
# 495   lib/ansible/executor/task_queue_manager.py      0
# 1202                        tornado/websocket.py      0
# 1882                     lib/ansible/cli/pull.py      1
# 576                       salt/states/archive.py      1
# 3130       lib/ansible/modules/system/systemd.py      0
# 317                    flask/testsuite/appctx.py      0
# 1627                          bandit/cli/main.py      0
# 452      lib/ansible/modules/system/firewalld.py      0
# 823                    plugins/generic/search.py      0
# 
# ============================================================
# 
## }}}

## {{{ inspecting source code
print("\nTRAINING DATASET:")
same = train["vulnerable_function_source"] == train["patched_function_source"]
print(f"same: {train.loc[same, "label"].mean().round(3)}")
print("\n" + "=" * 60)
print("\nTESTING DATASET:")
same = test["function_code"] == test["patched_function_source"]
print(f"same: {test.loc[same, "class"].mean().round(3)}")
# TRAINING DATASET:
# same: 0.457
# 
# ============================================================
# 
# TESTING DATASET:
# same: 0.471

## }}}

## {{{ processing dataset
h1 = train[[
  "repo",
  "vulnerable_function_source",
  "patched_function_source",
  "label"
]]
h1.columns = ["repo", "source_code", "patch", "is_vulnerable"]

h2 = test[[
  "repo",
  "function_code",
  "patched_function_source",
  "class"
]]
h2.columns = ["repo", "source_code", "patch", "is_vulnerable"]

df = pd.concat([h1, h2], ignore_index=True)
df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)
print(df.sample(10, random_state=SEED))
#                        repo                                        source_code                                              patch  is_vulnerable
# 10831       ansible/ansible  def test_update_interval_larger_than_existing_...  def test_update_interval_larger_than_existing_...              1
# 12610        apache/airflow  def test_cli_assets_materialize(parser: Argume...  def test_cli_assets_materialize(parser: Argume...              1
# 14713        saltstack/salt  def _run(cmd,\n         cwd=None,\n         st...  def _run(cmd,\n         cwd=None,\n         st...              1
# 9520         apache/airflow  def get_conn(self):\n        conn = self.get_c...  def get_conn(self):\n        conn = self.get_c...              0
# 1201   sqlmapproject/sqlmap  def getFingerprint(self):\n        value = ""\...  def getFingerprint(self):\n        value = ""\...              0
# 1137     tornadoweb/tornado  def _value_from_stopiteration(e):\n    try:\n ...  def _value_from_stopiteration(e):\n    try:\n ...              0
# 16152        apache/airflow  def test_parms_not_passed_is_empty_dict(self):...  def test_parms_not_passed_is_empty_dict(self):...              1
# 15519         django/django  def get_backend_timeout(self, timeout=DEFAULT_...  def get_backend_timeout(self, timeout=DEFAULT_...              0
# 14600         django/django  def test_chunked(self):\n        "The static v...  def test_chunked(self):\n        "The static v...              0
# 3779        ansible/ansible  def __init__(self):\n\n        super(CallbackM...  def __init__(self):\n\n        super(CallbackM...              0
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 17811 entries, 0 to 17810
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   repo           17811 non-null  str
#  1   source_code    17756 non-null  str
#  2   patch          17692 non-null  str
#  3   is_vulnerable  17811 non-null  int64
# dtypes: int64(1), str(3)
# memory usage: 556.7 KB
# None
#
# ast parsable check
import ast

def can_parse(source):
  try:
    ast.parse(source)
    return True
  except (SyntaxError, NameError, ValueError, TypeError):
    return False

source_code = df["source_code"].apply(can_parse)
patched_code = df["patch"].apply(can_parse)
print(f"Parsable source code: {source_code.sum()}")
print(f"Parsable patched code: {patched_code.sum()}")
# Parsable source code: 17756
# Parsable patched code: 17692
df = df[(source_code & patched_code)]
print(df.info())
# <class 'pandas.DataFrame'>
# Index: 17692 entries, 0 to 17809
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   repo           17692 non-null  str
#  1   source_code    17692 non-null  str
#  2   patch          17692 non-null  str
#  3   is_vulnerable  17692 non-null  int64
# dtypes: int64(1), str(3)
# memory usage: 691.1 KB
# None
#
# saving dataset
filename = os.path.join(os.path.abspath(".."), "data", "processed", "dataset.csv")
df.to_csv(filename, index=False)
print(f"dataset saved at {filename}")
## }}}

## }}}

## {{{ new day, new beginning with processed dataset
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GroupShuffleSplit, GridSearchCV, GroupKFold
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
  accuracy_score,
  roc_auc_score,
  precision_score,
  recall_score,
  f1_score,
  balanced_accuracy_score,
  classification_report,
  confusion_matrix,
)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
##

## constanst
SEED = 3
##

## {{{ loading dataset
filename = os.path.join(os.path.abspath(".."), "data", "processed", "dataset.csv")
df = pd.read_csv(filename)
print(df.info())
print(df.sample(10, random_state=SEED))
# <class 'pandas.DataFrame'>
# RangeIndex: 17692 entries, 0 to 17691
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   repo           17692 non-null  str
#  1   source_code    17692 non-null  str
#  2   patch          17692 non-null  str
#  3   is_vulnerable  17692 non-null  int64
# dtypes: int64(1), str(3)
# memory usage: 553.0 KB
# None
#                        repo                                        source_code                                              patch  is_vulnerable
# 7198         apache/airflow  def test_gen_pod_extract_xcom(self, mock_rand_...  def test_gen_pod_extract_xcom(self, mock_rand_...              1
# 13839       ansible/ansible  def __init__(self):\n        self.supports_che...  def __init__(self):\n        self.supports_che...              0
# 16345  sqlmapproject/sqlmap  def getColumns(self, onlyColNames=False, colTu...  def getColumns(self, onlyColNames=False, colTu...              0
# 12166        saltstack/salt  def present(\n    name,\n    skip_translate=No...  def present(\n    name,\n    skip_translate=No...              1
# 2314          mlflow/mlflow  def test_crud_prompts(tracking_uri):\n    clie...  def test_crud_prompts(tracking_uri):\n    clie...              1
# 5806         saltstack/salt  def _thread_return(self, data):\n        '''\n...  def _thread_return(self, data):\n        '''\n...              1
# 6256         saltstack/salt  def test_configparser():\n    data = {"foo": {...  def test_configparser():\n    data = {"foo": {...              1
# 1999         apache/airflow  def test_next_run_assets(test_client, dag_make...  def test_next_run_assets(test_client, dag_make...              1
# 13691         django/django  def _has_changed(self, initial, data):\n      ...  def _has_changed(self, initial, data):\n      ...              0
# 5491        ansible/ansible  def load_config(module, command_filter, commit...  def load_config(module, command_filter, commit...              0
## }}}

## {{{ splitting
splitter = GroupShuffleSplit(
  n_splits=1,
  test_size=0.15,
  random_state=SEED,
)

train_val_idx, test_idx = next(splitter.split(
  df["source_code"],
  df["is_vulnerable"],
  groups=df["patch"],
))

train_val = df.iloc[train_val_idx].reset_index(drop=True)
test = df.iloc[test_idx].reset_index(drop=True)

splitter = GroupShuffleSplit(
  n_splits=1,
  test_size=0.17647,
  random_state=SEED,
)

train_idx, val_idx = next(splitter.split(
  train_val["source_code"],
  train_val["is_vulnerable"],
  groups=train_val["patch"],
))

train = train_val.iloc[train_idx].reset_index(drop=True)
val = train_val.iloc[val_idx].reset_index(drop=True)

train_groups = set(train["patch"])
val_groups = set(val["patch"])
test_groups = set(test["patch"])
assert(train_groups.isdisjoint(val_groups))
assert(val_groups.isdisjoint(test_groups))
assert(test_groups.isdisjoint(train_groups))
for name, df in [
  ("Train", train),
  ("Val", val),
  ("Test", test),
]:
  print(name.upper())
  print(df["is_vulnerable"].value_counts(normalize=True))
# 
# TRAIN
# is_vulnerable
# 0    0.558786
# 1    0.441214
# Name: proportion, dtype: float64
# VAL
# is_vulnerable
# 0    0.561417
# 1    0.438583
# Name: proportion, dtype: float64
# TEST
# is_vulnerable
# 0    0.550113
# 1    0.449887
# Name: proportion, dtype: float64
# 
## }}}
#
## {{{ encoding source code
vectorizer = TfidfVectorizer(
  token_pattern=r"(?u)\b\w+\b",
  analyzer="word",
  # unigram -- individual tokens
  # bigram -- pairs of consecutive tokens
  ngram_range=(1, 2),
)

X_train = vectorizer.fit_transform(train["source_code"])
y_train = train["is_vulnerable"].values
X_val = vectorizer.transform(val["source_code"])
y_val = val["is_vulnerable"].values
# inspecting vectorizer
row = pd.DataFrame({
  "tokens": vectorizer.get_feature_names_out(),
  "idf": vectorizer.idf_,
})

print("IDF ASCENDING=FALSE")
print(row.sort_values("idf", ascending=False).head(20))
# IDF ASCENDING=FALSE
#                       tokens       idf
# 653351  šđćžćžšđ šđabcćžćžšđ  9.731094
# 653350      šđćžćžšđ choices  9.731094
# 653349              šđćžćžšđ  9.731094
# 653348      šđabcćžćžšđ ćžšđ  9.731094
# 653347           šđabcćžćžšđ  9.731094
# 653346          ćžšđ abcćžšđ  9.731094
# 653345                  ćžšđ  9.731094
# 653344               üniçø é  9.731094
# 31                  0 0x1000  9.731094
# 28                     0 0na  9.731094
# 27                      0 09  9.731094
# 25                      0 07  9.731094
# 21                      0 03  9.731094
# 16                     0 008  9.731094
# 653343                 üniçø  9.731094
# 653342         é assert_copy  9.731094
# 653341                     é  9.731094
# 653340                   ç d  9.731094
# 653339                     ç  9.731094
# 653338            æøå skaper  9.731094
print(train["source_code"].iloc[0])
# def test_model_save_persists_specified_conda_env_in_mlflow_model_directory(
#         model, model_path, keras_custom_env):
#     mlflow.keras.save_model(keras_model=model, path=model_path, conda_env=keras_custom_env)
# 
#     pyfunc_conf = _get_flavor_configuration(model_path=model_path, flavor_name=pyfunc.FLAVOR_NAME)
#     saved_conda_env_path = os.path.join(model_path, pyfunc_conf[pyfunc.ENV])
#     assert os.path.exists(saved_conda_env_path)
#     assert saved_conda_env_path != keras_custom_env
# 
#     with open(keras_custom_env, "r") as f:
#         keras_custom_env_parsed = yaml.safe_load(f)
#     with open(saved_conda_env_path, "r") as f:
#         saved_conda_env_parsed = yaml.safe_load(f)
#     assert saved_conda_env_parsed == keras_custom_env_parsed
suspicious = "šđćžćžšđ"
mask = train["source_code"].str.contains(
  suspicious,
  regex=False
)
print(train.loc[mask, ["repo", "source_code", "is_vulnerable"]])
# Empty DataFrame
# Columns: [repo, source_code, is_vulnerable]
# Index: []
# 
# confusing🤔 na??? where does this token came from in vectorizer?
print("\nUnique tokens:")
print(row["tokens"].value_counts())
print("\nVocabulary size:", len(vectorizer.vocabulary_))
print("\nTraining matrix shape: ", X_train.shape)
print("\nNonzero values: ", X_train.nnz)
print("\nSparasity: ", 1 - X_train.nnz / (X_train.shape[0] * X_train.shape[1]))
# Unique tokens:
# tokens
# 0                        1
# 0 0                      1
# 0 00                     1
# 0 0000                   1
# 0 000000                 1
#                         ..
# метка_оператора_2 tag    1
# 以下为主机名解析                 1
# 以下为主机名解析 ccc             1
# 本机                       1
# 本机 fopen_mock            1
# Name: count, Length: 653377, dtype: int64
# 
# Vocabulary size: 653377
# 
# Training matrix shape:  (12384, 653377)
# 
# Nonzero values:  3189762
# 
# Sparasity:  0.9996057846833754
tokens = vectorizer.get_feature_names_out()
suspicious_tokens = [
  token for token in tokens
  if any(ord(char) > 127 for char in token)
]
for token in suspicious_tokens[:20]:
  print(repr(token))
# '200 déplacé'
# 'a sťāçkeð'
# 'a tãbűlař'
# 'a α'
# 'abcćžšđ'
# 'abcćžšđ ul'
# 'amp β'
# 'andré'
# 'andré bessette'
# 'anton α'
# 'anöther'
# 'anöther sťāçkeð'
# 'assert räksmörgås'
# 'assertserializedequal föobár'
# 'awεšome'
# 'awεšome pubdate'
# 'awεšome slug1'
# 'awεšomeıııi'
# 'awεšomeıııi pubdate'
# 'awεšomeıııi self'
token = suspicious_tokens[0]
print(repr(token))
print([hex(ord(char)) for char in token])
# '200 déplacé'
# ['0x32', '0x30', '0x30', '0x20', '0x64', '0xe9', '0x70', '0x6c', '0x61', '0x63', '0xe9']
analyzer = vectorizer.build_analyzer()
for i, source in enumerate(train["source_code"]):
  found = [t for t in analyzer(source) if t in suspicious_tokens]
  if found:
    print("ROW: ", i)
    print("TOKENS: ", [repr(t) for t in found])
    print(source[:1000])
    break
# ROW:  381
# TOKENS:  ["'nàmë'", "'awεšomeıııi'", "'sťāçkeð'", "'anöther'", "'sťāçkeð'", "'tãbűlař'", "'tãbűlař'", "'nàmë'", "'awεšomeıııi'", "'nàmë'", "'awεšomeıııi'", "'sťāçkeð'", "'anöther'", "'sťāçkeð'", "'tãbűlař'", "'tãbűlař'", "'main nàmë'", "'nàmë and'", "'s awεšomeıııi'", "'awεšomeıııi slug1'", "'a sťāçkeð'", "'sťāçkeð inline'", "'have anöther'", "'anöther sťāçkeð'", "'sťāçkeð inline'", "'a tãbűlař'", "'tãbűlař inline'", "'a tãbűlař'", "'tãbűlař inline'", "'main nàmë'", "'nàmë and'", "'s awεšomeıııi'", "'awεšomeıııi pubdate'", "'main nàmë'", "'nàmë and'", "'its awεšomeıııi'", "'awεšomeıııi self'", "'a sťāçkeð'", "'sťāçkeð inline'", "'have anöther'", "'anöther sťāçkeð'", "'sťāçkeð inline'", "'a tãbűlař'", "'tãbűlař inline'", "'a tãbűlař'", "'tãbűlař inline'"]
# def test_prepopulated_fields(self):
#         """
#         The JavaScript-automated prepopulated fields work with the main form
#         and with stacked and tabular inlines.
#         Refs #13068, #9264, #9983, #9784.
#         """
#         self.admin_login(username='super', password='secret', login_url=reverse('admin:index'))
#         self.selenium.get(self.live_server_url + reverse('admin:admin_views_mainprepopulated_add'))
#         self.wait_for('.select2')
# 
#         # Main form ----------------------------------------------------------
#         self.selenium.find_element_by_id('id_pubdate').send_keys('2012-02-18')
#         self.select_option('#id_status', 'option two')
#         self.selenium.find_element_by_id('id_name').send_keys(' this is the mAin nÀMë and it\'s awεšomeıııİ')
#         slug1 = self.selenium.find_element_by_id('id_slug1').get_attribute('value')
#         slug2 = self.selenium.find_element_by_id('id_slug2').get_attribute('value')
#         slug3 = self.selenium.find_element_by_id('id_
#
# good, but we haven't found the suspicious token we were looking for
# yet...
target = "šđćžćžšđ"
print("In Vocabulary: ", target in vectorizer.vocabulary_)
for i, source in enumerate(train["source_code"]):
  if target in analyzer(source):
    print("Found in row: ", i)
    print("Repository name: ", train.iloc[i]["repo"])
    print(source)
    break
# {{{ output -- too big
# In Vocabulary:  True
# Found in row:  2634
# Repository name:  django/django
# def test_checkboxselectmultiple(self):
#         w = CheckboxSelectMultiple()
#         self.assertHTMLEqual(w.render('beatles', ['J'], choices=(('J', 'John'), ('P', 'Paul'), ('G', 'George'), ('R', 'Ringo'))), """<ul>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="J" /> John</label></li>
# <li><label><input type="checkbox" name="beatles" value="P" /> Paul</label></li>
# <li><label><input type="checkbox" name="beatles" value="G" /> George</label></li>
# <li><label><input type="checkbox" name="beatles" value="R" /> Ringo</label></li>
# </ul>""")
#         self.assertHTMLEqual(w.render('beatles', ['J', 'P'], choices=(('J', 'John'), ('P', 'Paul'), ('G', 'George'), ('R', 'Ringo'))), """<ul>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="J" /> John</label></li>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="P" /> Paul</label></li>
# <li><label><input type="checkbox" name="beatles" value="G" /> George</label></li>
# <li><label><input type="checkbox" name="beatles" value="R" /> Ringo</label></li>
# </ul>""")
#         self.assertHTMLEqual(w.render('beatles', ['J', 'P', 'R'], choices=(('J', 'John'), ('P', 'Paul'), ('G', 'George'), ('R', 'Ringo'))), """<ul>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="J" /> John</label></li>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="P" /> Paul</label></li>
# <li><label><input type="checkbox" name="beatles" value="G" /> George</label></li>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="R" /> Ringo</label></li>
# </ul>""")
# 
#         # If the value is None, none of the options are selected:
#         self.assertHTMLEqual(w.render('beatles', None, choices=(('J', 'John'), ('P', 'Paul'), ('G', 'George'), ('R', 'Ringo'))), """<ul>
# <li><label><input type="checkbox" name="beatles" value="J" /> John</label></li>
# <li><label><input type="checkbox" name="beatles" value="P" /> Paul</label></li>
# <li><label><input type="checkbox" name="beatles" value="G" /> George</label></li>
# <li><label><input type="checkbox" name="beatles" value="R" /> Ringo</label></li>
# </ul>""")
# 
#         # If the value corresponds to a label (but not to an option value), none of the options are selected:
#         self.assertHTMLEqual(w.render('beatles', ['John'], choices=(('J', 'John'), ('P', 'Paul'), ('G', 'George'), ('R', 'Ringo'))), """<ul>
# <li><label><input type="checkbox" name="beatles" value="J" /> John</label></li>
# <li><label><input type="checkbox" name="beatles" value="P" /> Paul</label></li>
# <li><label><input type="checkbox" name="beatles" value="G" /> George</label></li>
# <li><label><input type="checkbox" name="beatles" value="R" /> Ringo</label></li>
# </ul>""")
# 
#         # If multiple values are given, but some of them are not valid, the valid ones are selected:
#         self.assertHTMLEqual(w.render('beatles', ['J', 'G', 'foo'], choices=(('J', 'John'), ('P', 'Paul'), ('G', 'George'), ('R', 'Ringo'))), """<ul>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="J" /> John</label></li>
# <li><label><input type="checkbox" name="beatles" value="P" /> Paul</label></li>
# <li><label><input checked="checked" type="checkbox" name="beatles" value="G" /> George</label></li>
# <li><label><input type="checkbox" name="beatles" value="R" /> Ringo</label></li>
# </ul>""")
# 
#         # The value is compared to its str():
#         self.assertHTMLEqual(w.render('nums', [2], choices=[('1', '1'), ('2', '2'), ('3', '3')]), """<ul>
# <li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>
# <li><label><input checked="checked" type="checkbox" name="nums" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>
# </ul>""")
#         self.assertHTMLEqual(w.render('nums', ['2'], choices=[(1, 1), (2, 2), (3, 3)]), """<ul>
# <li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>
# <li><label><input checked="checked" type="checkbox" name="nums" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>
# </ul>""")
#         self.assertHTMLEqual(w.render('nums', [2], choices=[(1, 1), (2, 2), (3, 3)]), """<ul>
# <li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>
# <li><label><input checked="checked" type="checkbox" name="nums" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>
# </ul>""")
# 
#         # The 'choices' argument can be any iterable:
#         def get_choices():
#             for i in range(5):
#                 yield (i, i)
#         self.assertHTMLEqual(w.render('nums', [2], choices=get_choices()), """<ul>
# <li><label><input type="checkbox" name="nums" value="0" /> 0</label></li>
# <li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>
# <li><label><input checked="checked" type="checkbox" name="nums" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>
# <li><label><input type="checkbox" name="nums" value="4" /> 4</label></li>
# </ul>""")
# 
#         # You can also pass 'choices' to the constructor:
#         w = CheckboxSelectMultiple(choices=[(1, 1), (2, 2), (3, 3)])
#         self.assertHTMLEqual(w.render('nums', [2]), """<ul>
# <li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>
# <li><label><input checked="checked" type="checkbox" name="nums" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>
# </ul>""")
# 
#         # If 'choices' is passed to both the constructor and render(), then they'll both be in the output:
#         self.assertHTMLEqual(w.render('nums', [2], choices=[(4, 4), (5, 5)]), """<ul>
# <li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>
# <li><label><input checked="checked" type="checkbox" name="nums" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>
# <li><label><input type="checkbox" name="nums" value="4" /> 4</label></li>
# <li><label><input type="checkbox" name="nums" value="5" /> 5</label></li>
# </ul>""")
# 
#         # Choices are escaped correctly
#         self.assertHTMLEqual(w.render('escape', None, choices=(('bad', 'you & me'), ('good', mark_safe('you &gt; me')))), """<ul>
# <li><label><input type="checkbox" name="escape" value="1" /> 1</label></li>
# <li><label><input type="checkbox" name="escape" value="2" /> 2</label></li>
# <li><label><input type="checkbox" name="escape" value="3" /> 3</label></li>
# <li><label><input type="checkbox" name="escape" value="bad" /> you &amp; me</label></li>
# <li><label><input type="checkbox" name="escape" value="good" /> you &gt; me</label></li>
# </ul>""")
# 
#         # Unicode choices are correctly rendered as HTML
#         self.assertHTMLEqual(w.render('nums', ['ŠĐĆŽćžšđ'], choices=[('ŠĐĆŽćžšđ', 'ŠĐabcĆŽćžšđ'), ('ćžšđ', 'abcćžšđ')]), '<ul>\n<li><label><input type="checkbox" name="nums" value="1" /> 1</label></li>\n<li><label><input type="checkbox" name="nums" value="2" /> 2</label></li>\n<li><label><input type="checkbox" name="nums" value="3" /> 3</label></li>\n<li><label><input checked="checked" type="checkbox" name="nums" value="\u0160\u0110\u0106\u017d\u0107\u017e\u0161\u0111" /> \u0160\u0110abc\u0106\u017d\u0107\u017e\u0161\u0111</label></li>\n<li><label><input type="checkbox" name="nums" value="\u0107\u017e\u0161\u0111" /> abc\u0107\u017e\u0161\u0111</label></li>\n</ul>')
# 
#         # Each input gets a separate ID
#         self.assertHTMLEqual(CheckboxSelectMultiple().render('letters', list('ac'), choices=zip(list('abc'), list('ABC')), attrs={'id': 'abc'}), """<ul id="abc">
# <li><label for="abc_0"><input checked="checked" type="checkbox" name="letters" value="a" id="abc_0" /> A</label></li>
# <li><label for="abc_1"><input type="checkbox" name="letters" value="b" id="abc_1" /> B</label></li>
# <li><label for="abc_2"><input checked="checked" type="checkbox" name="letters" value="c" id="abc_2" /> C</label></li>
# </ul>""")
# 
#         # Each input gets a separate ID when the ID is passed to the constructor
#         self.assertHTMLEqual(CheckboxSelectMultiple(attrs={'id': 'abc'}).render('letters', list('ac'), choices=zip(list('abc'), list('ABC'))), """<ul id="abc">
# <li><label for="abc_0"><input checked="checked" type="checkbox" name="letters" value="a" id="abc_0" /> A</label></li>
# <li><label for="abc_1"><input type="checkbox" name="letters" value="b" id="abc_1" /> B</label></li>
# <li><label for="abc_2"><input checked="checked" type="checkbox" name="letters" value="c" id="abc_2" /> C</label></li>
# </ul>""")
# 
#         w = CheckboxSelectMultiple()
#         r = w.get_renderer('abc', 'b', choices=[(c, c.upper()) for c in 'abc'])
#         # You can iterate over the CheckboxFieldRenderer to get individual elements
#         expected = [
#             '<label><input type="checkbox" name="abc" value="a" /> A</label>',
#             '<label><input checked="checked" type="checkbox" name="abc" value="b" /> B</label>',
#             '<label><input type="checkbox" name="abc" value="c" /> C</label>',
#         ]
#         for output, expected in zip(r, expected):
#             self.assertHTMLEqual(force_text(output), expected)
# 
#         # You can access individual elements
#         self.assertHTMLEqual(force_text(r[1]),
#             '<label><input checked="checked" type="checkbox" name="abc" value="b" /> B</label>')
# 
#         # Out-of-range errors are propagated
#         with self.assertRaises(IndexError):
#             r[42]
## }}}
#
print("IDF ASCENDING=TRUE")
print(row.sort_values("idf", ascending=True).head(20))
# IDF ASCENDING=TRUE
#         tokens       idf
# 155070     def  1.000000
# 276009      if  1.484791
# 504798    self  1.508809
# 286165      in  1.519611
# 582745     the  1.576450
# 231981     for  1.646532
# 479521  return  1.687270
# 388823     not  1.699384
# 593799      to  1.736293
# 304997      is  1.741195
# 384296    none  1.775143
# 38854        a  1.793541
# 0            0  1.811556
# 56001      and  1.830828
# 642963    with  1.887049
# 4176         1  1.894132
# 602021    true  1.939158
# 188319    else  2.002238
# 216841   false  2.084979
# 69316       as  2.094342
row = pd.DataFrame({
  "tokens": vectorizer.get_feature_names_out()[
    X_train[0].indices
  ],
  "tfidf": X_train[0].data,
})
print("TFIDF ASCENDING=FALSE")
print(row[row["tfidf"] > 0].sort_values("tfidf", ascending=False).head(20))
# TFIDF ASCENDING=FALSE
#                                    tokens     tfidf
# 4                        keras_custom_env  0.395932
# 15                   saved_conda_env_path  0.334735
# 3                              model_path  0.300193
# 26                keras_custom_env_parsed  0.197966
# 29                 saved_conda_env_parsed  0.175616
# 11                            pyfunc_conf  0.155662
# 74                            safe_load f  0.149184
# 28                              safe_load  0.126528
# 73                         yaml safe_load  0.126528
# 13                            flavor_name  0.125637
# 25                                      f  0.120798
# 69                                   r as  0.107706
# 14                                 pyfunc  0.107113
# 34                keras_custom_env mlflow  0.098983
# 64  saved_conda_env_path keras_custom_env  0.098983
# 67                  open keras_custom_env  0.098983
# 65                  keras_custom_env with  0.098983
# 68                     keras_custom_env r  0.098983
# 43           keras_custom_env pyfunc_conf  0.098983
# 72           keras_custom_env_parsed yaml  0.098983
print("TFIDF ASCENDING=TRUE")
print(row[row["tfidf"] > 0].sort_values("tfidf", ascending=True).head(20))
# TFIDF ASCENDING=TRUE
#              tokens     tfidf
# 0               def  0.010172
# 17             join  0.027698
# 20           exists  0.036184
# 53        path join  0.036751
# 21             with  0.038389
# 5            mlflow  0.038428
# 24               as  0.042607
# 60      path exists  0.044473
# 18              env  0.046713
# 16               os  0.056444
# 7        save_model  0.057507
# 23                r  0.061487
# 52          os path  0.063937
# 10        conda_env  0.064218
# 59        assert os  0.066040
# 40  path model_path  0.068015
# 39       model path  0.068260
# 19           assert  0.070406
# 6             keras  0.071104
# 2             model  0.071579
## }}}

## {{{ baseline model
dummy = DummyClassifier(strategy="most_frequent", random_state=SEED)
dummy.fit(X_train, y_train)
y_dummy = dummy.predict(X_val)
print(f"Accuracy: {accuracy_score(y_val, y_dummy)}")
print(f"Balanced Accuracy: {balanced_accuracy_score(y_val, y_dummy)}")

print(f"classification report:\n{classification_report(y_val, y_dummy, zero_division=0)}")
print(f"confusion matrix:\n{confusion_matrix(y_val, y_dummy)}")
# Accuracy: 0.5614167294649586
# Balanced Accuracy: 0.5
# classification report:
#               precision    recall  f1-score   support
# 
#            0       0.56      1.00      0.72      1490
#            1       0.00      0.00      0.00      1164
# 
#     accuracy                           0.56      2654
#    macro avg       0.28      0.50      0.36      2654
# weighted avg       0.32      0.56      0.40      2654
# 
# confusion matrix:
# [[1490    0]
#  [1164    0]]
model = LogisticRegression(
  # works better in comparision to other solver
  # when previously compared it
  solver="lbfgs",
  C=1.0,
  max_iter=1000,
)
model.fit(X_train, y_train)
y_pred = model.predict(X_val)
y_prob = model.predict_proba(X_val)[:, 1]
print(f"Accuracy: {accuracy_score(y_val, y_pred)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_pred)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_prob)}")
print(f"Classification report:\n{classification_report(y_val, y_pred, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")
# Accuracy: 0.9125847776940467
# Balanced accuracy: 0.9092720081182684
# ROC_AUC Score: 0.9684137088032474
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.91      0.94      0.92      1490
#            1       0.92      0.88      0.90      1164
# 
#     accuracy                           0.91      2654
#    macro avg       0.91      0.91      0.91      2654
# weighted avg       0.91      0.91      0.91      2654
# 
# Confusion Matrix:
# [[1395   95]
#  [ 137 1027]]
# 
models = {
  "Dummy": y_dummy,
  "Logistic Regression": y_pred,
}
for name, predictions in models.items():
  print(f"\n{name}:")
  print("Accuracy: ", accuracy_score(y_val, predictions))
  print("Balanced Accuracy: ", balanced_accuracy_score(y_val, predictions))
  print("F1: ", f1_score(y_val, predictions, zero_division=0))
  print("Precision: ", precision_score(y_val, predictions, zero_division=0))
  print("Recall: ", recall_score(y_val, predictions, zero_division=0))
  print("\n" + "=" * 60)
# 
# Dummy:
# Accuracy:  0.5614167294649586
# Balanced Accuracy:  0.5
# F1:  0.0
# Precision:  0.0
# Recall:  0.0
# 
# ============================================================
# 
# Logistic Regression:
# Accuracy:  0.9125847776940467
# Balanced Accuracy:  0.9092720081182684
# F1:  0.8985126859142607
# Precision:  0.9153297682709447
# Recall:  0.8823024054982818
# 
# ============================================================
# 
# 😁😁😁 But wait, something is very fishy because other datasets we
# worked with hardly gave us like 30-60% accuracy, so it might be that
# our dataset is biased or something or might contains clues that our
# model can predict without actually learning anything about
# vulnerability like we seen django repo it might learn loopholes in it.
#
# more investigating
train_repos = set(train["repo"])
val_repos = set(val["repo"])
test_repos = set(test["repo"])
print("Train repositories: ", len(train_repos))
print("Val repositories: ", len(val_repos))
print("Test repositories: ", len(test_repos))
print("Train n Validation: ", len(train_repos & val_repos))
print("Validation n Test: ", len(val_repos & test_repos))
print("Test n Train: ", len(test_repos & train_repos))
# Train repositories:  15
# Val repositories:  15
# Test repositories:  15
# Train n Validation:  15
# Validation n Test:  15
# Test n Train:  15
#
# see there's an overlap it might be the reason why we have > 90% accuracy
train_sources = set(train["source_code"])
val_sources = set(val["source_code"])
test_sources = set(test["source_code"])
print("Train n Validation:", len(train_sources & val_sources))
print("Validation n Test:", len(val_sources & test_sources))
print("Test n Train:", len(test_sources & train_sources))
# Train n Validation: 0
# Validation n Test: 0
# Test n Train: 0
# 
## }}}

## {{{ split by repo
## {{{ splitting
filename = os.path.join(os.path.abspath(".."), "data", "processed", "dataset.csv")
df = pd.read_csv(filename)
splitter = GroupShuffleSplit(
  n_splits=1,
  test_size=0.15,
  random_state=SEED,
)

train_val_idx, test_idx = next(splitter.split(
  df["source_code"],
  df["is_vulnerable"],
  groups=df["repo"],
))

train_val = df.iloc[train_val_idx].reset_index(drop=True)
test = df.iloc[test_idx].reset_index(drop=True)

splitter = GroupShuffleSplit(
  n_splits=1,
  test_size=0.17647,
  random_state=SEED,
)

train_idx, val_idx = next(splitter.split(
  train_val["source_code"],
  train_val["is_vulnerable"],
  groups=train_val["repo"],
))

train = train_val.iloc[train_idx].reset_index(drop=True)
val = train_val.iloc[val_idx].reset_index(drop=True)

train_repos = set(train["repo"])
val_repos = set(val["repo"])
test_repos = set(test["repo"])
print("Repositories Overlap:")
print("Train n Validation: ", len(train_repos & val_repos))
print("Validation n Test: ", len(val_repos & test_repos))
print("Test n Train: ", len(test_repos & train_repos))
# Repositories Overlap:
# Train n Validation:  0
# Validation n Test:  0
# Test n Train:  0
train_sources = set(train["source_code"])
val_sources = set(val["source_code"])
test_sources = set(test["source_code"])
print("Source Code Overlap:")
print("Train n Validation: ", len(train_sources & val_sources))
print("Validation n Test: ", len(val_sources & test_sources))
print("Test n Train: ", len(test_sources & train_sources))
# Source Code Overlap:
# Train n Validation:  0
# Validation n Test:  0
# Test n Train:  0
train_patch = set(train["patch"])
val_patch = set(val["patch"])
test_patch = set(test["patch"])
print("Patch Code Overlap:")
print("Train n Validation: ", len(train_patch & val_patch))
print("Validation n Test: ", len(val_patch & test_patch))
print("Test n Train: ", len(test_patch & train_patch))
# Patch Code Overlap:
# Train n Validation:  0
# Validation n Test:  0
# Test n Train:  2
print("Class distribution:")
print("Train:\n", train["is_vulnerable"].value_counts(normalize=True))
print("Validation:\n", val["is_vulnerable"].value_counts(normalize=True))
print("Test:\n", test["is_vulnerable"].value_counts(normalize=True))
# Class distribution:
# Train:
#  is_vulnerable
# 0    0.511733
# 1    0.488267
# Name: proportion, dtype: float64
# Validation:
#  is_vulnerable
# 0    0.580464
# 1    0.419536
# Name: proportion, dtype: float64
# Test:
#  is_vulnerable
# 0    0.649575
# 1    0.350425
# Name: proportion, dtype: float64
print("Size:")
print("Train: ", train.shape)
print("Validation: ", val.shape)
print("Test: ", test.shape)
# Size:
# Train:  (9716, 4)
# Validation:  (4095, 4)
# Test:  (3881, 4)
## }}}
## {{{ vectorizer
vectorizer = TfidfVectorizer(
  token_pattern=r"(?u)\b\w+\b",
  analyzer="word",
  ngram_range=(1, 2),
)

X_train = vectorizer.fit_transform(train["source_code"])
y_train = train["is_vulnerable"].values
X_val = vectorizer.transform(val["source_code"])
y_val = val["is_vulnerable"].values
## }}}
## {{{ model
dummy = DummyClassifier(strategy="most_frequent", random_state=SEED)
dummy.fit(X_train, y_train)
y_dummy = dummy.predict(X_val)
print(f"Accuracy: {accuracy_score(y_val, y_dummy)}")
print(f"Balanced Accuracy: {balanced_accuracy_score(y_val, y_dummy)}")

print(f"classification report:\n{classification_report(y_val, y_dummy, zero_division=0)}")
print(f"confusion matrix:\n{confusion_matrix(y_val, y_dummy)}")
# Accuracy: 0.5804639804639805
# Balanced Accuracy: 0.5
# classification report:
#               precision    recall  f1-score   support
# 
#            0       0.58      1.00      0.73      2377
#            1       0.00      0.00      0.00      1718
# 
#     accuracy                           0.58      4095
#    macro avg       0.29      0.50      0.37      4095
# weighted avg       0.34      0.58      0.43      4095
# 
# confusion matrix:
# [[2377    0]
#  [1718    0]]
# 
model = LogisticRegression(
  solver="lbfgs",
  C=1.0,
  max_iter=1000,
)
model.fit(X_train, y_train)
y_pred = model.predict(X_val)
y_prob = model.predict_proba(X_val)[:, 1]
print(f"Accuracy: {accuracy_score(y_val, y_pred)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_pred)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_prob)}")
print(f"Classification report:\n{classification_report(y_val, y_pred, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")
# Accuracy: 0.8273504273504273
# Balanced accuracy: 0.8098907457625293
# ROC_AUC Score: 0.8638739609264767
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.81      0.92      0.86      2377
#            1       0.86      0.70      0.77      1718
# 
#     accuracy                           0.83      4095
#    macro avg       0.84      0.81      0.82      4095
# weighted avg       0.83      0.83      0.82      4095
# 
# Confusion Matrix:
# [[2183  194]
#  [ 513 1205]]
# 
models = {
  "Dummy": y_dummy,
  "Logistic Regression": y_pred,
}
for name, predictions in models.items():
  print(f"\n{name}:")
  print("Accuracy: ", accuracy_score(y_val, predictions))
  print("Balanced Accuracy: ", balanced_accuracy_score(y_val, predictions))
  print("F1: ", f1_score(y_val, predictions, zero_division=0))
  print("Precision: ", precision_score(y_val, predictions, zero_division=0))
  print("Recall: ", recall_score(y_val, predictions, zero_division=0))
  print("\n" + "=" * 60)
# 
# Dummy:
# Accuracy:  0.5804639804639805
# Balanced Accuracy:  0.5
# F1:  0.0
# Precision:  0.0
# Recall:  0.0
# 
# ============================================================
# 
# Logistic Regression:
# Accuracy:  0.8273504273504273
# Balanced Accuracy:  0.8098907457625293
# F1:  0.7731793391081168
# Precision:  0.8613295210864903
# Recall:  0.7013969732246799
# 
# ============================================================
# 
## }}}
## {{{ inspecting overlap patch in train & test
overlapping_patches = train_patch & test_patch
for patch in overlapping_patches:
  print("\nPATCH:")
  print(patch[:500])
  print("\nTRAIN:")
  print(train.loc[
    train["patch"] == patch,
    ["repo", "is_vulnerable", "source_code"]
  ])
  print("\nTEST:")
  print(test.loc[
    test["patch"] == patch,
    ["repo", "is_vulnerable", "source_code"]
  ])
  print("\n" + "=" * 60)
# PATCH:
# def __unionTestByCharBruteforce(comment):
#     """
#     This method tests if the target url is affected by an inband
#     SQL injection vulnerability. The test is done up to 50 columns
#     on the target database table
#     """
# 
#     query = agent.prefixQuery("UNION ALL SELECT %s" % conf.uChar)
# 
#     for count in range(conf.uColsStart, conf.uColsStop+1):
#         if kb.dbms == DBMS.ORACLE and query.endswith(" FROM DUAL"):
#             query = query[:-len(" FROM DUAL")]
# 
#         if count:
#             quer
# 
# TRAIN:
#                       repo  is_vulnerable                                        source_code
# 7459  sqlmapproject/sqlmap              0  def __unionTestByCharBruteforce(comment):\n   ...
# 
# TEST:
#                     repo  is_vulnerable                                        source_code
# 3287  andresriancho/w3af              0  def __unionTestByCharBruteforce(comment):\n   ...
# 
# ============================================================
# 
# PATCH:
# def checkDependencies():
#     missing_libraries = set()
# 
#     for dbmsName, data in DBMS_DICT.items():
#         if data[1] is None:
#             continue
# 
#         try:
#             if dbmsName in (DBMS.MSSQL, DBMS.SYBASE):
#                 import _mssql
#                 import pymssql
# 
#                 if not hasattr(pymssql, "__version__") or pymssql.__version__ < "1.0.2":
#                     warnMsg = "'%s' third-party library must be " % data[1]
#                     warnMsg += "version >= 1.0.2 to wor
# 
# TRAIN:
#                       repo  is_vulnerable                                        source_code
# 4467  sqlmapproject/sqlmap              0  def checkDependencies():\n    missing_librarie...
# 
# TEST:
#                     repo  is_vulnerable                                        source_code
# 2236  andresriancho/w3af              0  def checkDependencies():\n    missing_librarie...
# 
# ============================================================
# 
## }}}
## {{{ finding code duplication
patch_repo_counts = df.groupby("patch")["repo"].nunique()
cross_repo_patches = patch_repo_counts[
  patch_repo_counts > 1
]
print("Patches appearing in multiple repos: ", len(cross_repo_patches))
print("Total rows belonging to these patches: ", 
  df["patch"].isin(cross_repo_patches.index).sum())
print("Number of affected repositories: ", 
  df[df["patch"].isin(cross_repo_patches.index)]["repo"].nunique())
# Patches appearing in multiple repos:  2
# Total rows belonging to these patches:  4
# Number of affected repositories:  2
# 
## }}}

## {{{ Linear SVM
svm = LinearSVC(
  max_iter=2000,
  C=1.0,
  random_state=SEED,
)
svm.fit(X_train, y_train)
y_svm = svm.predict(X_val)
y_svm_score =  svm.decision_function(X_val)
print("Accuracy: ", accuracy_score(y_val, y_svm))
print("Balanced Accuracy: ", balanced_accuracy_score(y_val, y_svm))
print("ROC-AUC: ", roc_auc_score(y_val, y_svm_score))
print(classification_report(y_val, y_svm, zero_division=0))
print(confusion_matrix(y_val, y_svm))
# Accuracy:  0.8454212454212454
# Balanced Accuracy:  0.8305398603124726
# ROC-AUC:  0.8970209756577759
#               precision    recall  f1-score   support
# 
#            0       0.83      0.92      0.87      2377
#            1       0.87      0.74      0.80      1718
# 
#     accuracy                           0.85      4095
#    macro avg       0.85      0.83      0.84      4095
# weighted avg       0.85      0.85      0.84      4095
# 
# [[2194  183]
#  [ 450 1268]]
## }}}
## }}}

## {{{ fine tuning linear SVM
pipeline = Pipeline([
  ("tfidf", TfidfVectorizer(
    token_pattern=r"(?u)\b\w+\b",
    analyzer="word",
    ngram_range=(1, 2),
  )),
  ("svm", LinearSVC(
    random_state=SEED,
    max_iter=2000,
  )),
])

param_grid = {
  'svm__C': [0.1, 1.0, 7.0, 10.0],
}

cv = GroupKFold(n_splits=3)

search = GridSearchCV(
  pipeline,
  param_grid,
  scoring="f1",
  cv=cv,
  n_jobs=-1,
  verbose=1,
)

search.fit(
  train["source_code"],
  train["is_vulnerable"],
  groups=train["repo"],
)

print(search.best_params_)
print(search.best_score_)
# Fitting 3 folds for each of 4 candidates, totalling 12 fits
# {'svm__C': 10.0}
# 0.6416392790875138
## }}}

## {{{ inspecting our tuned model
print(pd.DataFrame(search.cv_results_)[
  ["param_svm__C", "mean_test_score", "std_test_score"]
])
#    param_svm__C  mean_test_score  std_test_score
# 0           0.1         0.555520        0.249337
# 1           1.0         0.619352        0.245490
# 2           7.0         0.637560        0.238710
# 3          10.0         0.641639        0.237101
best_model = search.best_estimator_
y_pred = best_model.predict(val["source_code"])
y_score = best_model.decision_function(val["source_code"])
print(f"\nAccuracy: {accuracy_score(y_val, y_pred)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_pred)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_score)}")
print(f"\nClassification report:\n{classification_report(y_val, y_pred, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")
# Accuracy: 0.8488400488400488
# Balanced accuracy: 0.8363894775455312
# ROC_AUC Score: 0.9080372487012958
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.84      0.91      0.88      2377
#            1       0.86      0.76      0.81      1718
# 
#     accuracy                           0.85      4095
#    macro avg       0.85      0.84      0.84      4095
# weighted avg       0.85      0.85      0.85      4095
# 
# Confusion Matrix:
# [[2172  205]
#  [ 414 1304]]
# 
## }}}
## }}}

## {{{ ast encoding
##
import ast
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import numpy as np

%matplotlib tk
##

## {{{ feature extraction
def extract_ast_features(source):
  tree = ast.parse(source)
  counts = Counter(
    type(node).__name__
    for node in ast.walk(tree)
  )
  return {
    "num_functions": counts["FunctionDef"] + counts["AsyncFunctionDef"],
    "num_calls": counts["Call"],
    "num_if": counts["If"],
    "num_loops": counts["For"] + counts["AsyncFor"] + counts["While"],
    "num_try": counts["Try"] + counts["TryStar"],
    "num_imports": counts["Import"] + counts["ImportFrom"],
    "num_returns": counts["Return"],
    "num_assignments": counts["Assign"] + counts["AnnAssign"] + counts["AugAssign"],
    "num_nodes": sum(counts.values()),
  }

ast_train = pd.DataFrame(
  train["source_code"].apply(extract_ast_features).tolist()
)
print(ast_train.sample(5, random_state=SEED))
print(ast_train.describe())
#       num_functions  num_calls  num_if  num_loops  num_try  num_imports  num_returns  num_assignments  num_nodes
# 4762              1         24       0          0        0            0            0               13        290
# 5900              2          7       0          0        0            0            1                5        113
# 800               1        190     119         12       25            0           44              183       3705
# 9310              1          9       0          0        0            0            0                2        116
# 146               1         84      22          5        0            0            1               79       1280
#        num_functions    num_calls       num_if    num_loops      num_try  num_imports  num_returns  num_assignments    num_nodes
# count    9716.000000  9716.000000  9716.000000  9716.000000  9716.000000  9716.000000  9716.000000      9716.000000  9716.000000
# mean        1.140902    21.485694     6.378757     0.980445     0.575340     0.115068     1.269350        13.708522   352.095204
# std         0.964960    40.604459    17.000930     2.192822     1.643085     0.715921     2.898632        29.547625   696.188063
# min         1.000000     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000         0.000000     5.000000
# 25%         1.000000     4.000000     0.000000     0.000000     0.000000     0.000000     0.000000         2.000000    75.000000
# 50%         1.000000     9.000000     1.000000     0.000000     0.000000     0.000000     0.000000         5.000000   147.000000
# 75%         1.000000    21.000000     5.000000     1.000000     0.000000     0.000000     1.000000        12.000000   314.000000
# max        45.000000   401.000000   155.000000    20.000000    25.000000    29.000000    45.000000       270.000000  6604.000000
# 
print(ast_train.corr().round(2))
#                  num_functions  num_calls  num_if  num_loops  num_try  num_imports  num_returns  num_assignments  num_nodes
# num_functions             1.00       0.21    0.19       0.17     0.11         0.10         0.34             0.20       0.23
# num_calls                 0.21       1.00    0.87       0.77     0.62         0.17         0.51             0.87       0.97
# num_if                    0.19       0.87    1.00       0.74     0.65         0.10         0.63             0.94       0.93
# num_loops                 0.17       0.77    0.74       1.00     0.48         0.07         0.39             0.74       0.79
# num_try                   0.11       0.62    0.65       0.48     1.00         0.18         0.46             0.59       0.61
# num_imports               0.10       0.17    0.10       0.07     0.18         1.00         0.06             0.09       0.12
# num_returns               0.34       0.51    0.63       0.39     0.46         0.06         1.00             0.59       0.55
# num_assignments           0.20       0.87    0.94       0.74     0.59         0.09         0.59             1.00       0.94
# num_nodes                 0.23       0.97    0.93       0.79     0.61         0.12         0.55             0.94       1.00
print(ast_train.nunique().sort_values())
# num_functions        14
# num_imports          15
# num_try              19
# num_loops            21
# num_returns          34
# num_if              130
# num_assignments     196
# num_calls           261
# num_nodes          1417
# dtype: int64
plt.figure(figsize=(11, 8))
sns.heatmap(
  ast_train.corr(),
  annot=True,
  fmt=".2f",
  cmap="coolwarm",
  center=0,
  square=True,
)
plt.title("Ast Feature Correlation")
plt.tight_layout()
image = os.path.join(os.path.abspath(".."), "images", "ast_train_corr.png")
plt.savefig(image, dpi=300, bbox_inches="tight")
plt.show()
# saved at ../images/ast_train_corr.png
## }}}

## {{{ ast_train analysis
ast_analysis = ast_train.copy()
ast_analysis["target"] = train["is_vulnerable"].to_numpy()
print(ast_analysis.groupby("target").mean().T.round(2))
# target                0       1
# num_functions      1.09    1.19
# num_calls         19.50   23.56
# num_if             6.51    6.24
# num_loops          1.03    0.93
# num_try            0.50    0.65
# num_imports        0.13    0.10
# num_returns        1.46    1.07
# num_assignments   13.64   13.78
# num_nodes        324.37  381.15
features = ast_train.columns
fig, axes = plt.subplots(3, 3, figsize=(14, 12))
for feature, ax in zip(features, axes.flat):
  sns.boxplot(
    data=ast_analysis,
    x="target",
    y=feature,
    ax=ax,
  )
  ax.set_title(feature)
plt.tight_layout()
plt.savefig(
  os.path.join(os.path.abspath(".."), "images", "ast_boxplot.png"),
  dpi=300, bbox_inches="tight"
)
plt.show()
# saved at ../images/ast_boxplot.png
## }}}

## {{{ baseline model + tuned model
scaler = StandardScaler()
X_train = pd.DataFrame(train["source_code"].apply(extract_ast_features).to_dict()).T.apply(np.log1p)
X_val = pd.DataFrame(val["source_code"].apply(extract_ast_features).to_dict()).T.apply(np.log1p)
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
y_train = train["is_vulnerable"].values
y_val = val["is_vulnerable"].values
dummy = DummyClassifier(strategy="most_frequent", random_state=SEED)
dummy.fit(X_train_scaled, y_train)
y_pred = dummy.predict(X_val_scaled)
print(f"\nAccuracy: {accuracy_score(y_val, y_pred)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_pred)}")
print(f"\nClassification report:\n{classification_report(y_val, y_pred, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")
svm = LinearSVC(
  C=10.0,
  max_iter=2000,
  random_state=SEED,
)
svm.fit(X_train_scaled, y_train)
y_svm = svm.predict(X_val_scaled)
y_svm_score = svm.decision_function(X_val_scaled)
print(f"\nAccuracy: {accuracy_score(y_val, y_svm)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_svm)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_svm_score)}")
print(f"\nClassification report:\n{classification_report(y_val, y_svm, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_svm)}")
# 
# Accuracy: 0.5804639804639805
# Balanced accuracy: 0.5
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.58      1.00      0.73      2377
#            1       0.00      0.00      0.00      1718
# 
#     accuracy                           0.58      4095
#    macro avg       0.29      0.50      0.37      4095
# weighted avg       0.34      0.58      0.43      4095
# 
# Confusion Matrix:
# [[2377    0]
#  [1718    0]]
# 
# Accuracy: 0.7255189255189255
# Balanced accuracy: 0.7258867356598916
# ROC_AUC Score: 0.778626956137176
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.79      0.72      0.75      2377
#            1       0.66      0.73      0.69      1718
# 
#     accuracy                           0.73      4095
#    macro avg       0.72      0.73      0.72      4095
# weighted avg       0.73      0.73      0.73      4095
# 
# Confusion Matrix:
# [[1720  657]
#  [ 467 1251]]
# 
## }}}

## {{{ Combine TF-IDF and scaked AST
from scipy.sparse import hstack, csr_matrix

# TF-IDF features
X_train_tfidf = best_model.named_steps["tfidf"].transform(
    train["source_code"])
X_val_tfidf = best_model.named_steps["tfidf"].transform(
    val["source_code"])
X_train_combined = hstack([
  X_train_tfidf,
  csr_matrix(X_train_scaled),
])
X_val_combined = hstack([
  X_val_tfidf,
  csr_matrix(X_val_scaled),
])

# Train Linear SVM
combined_svm = LinearSVC(
  C=10.0,
  random_state=SEED,
  max_iter=2000,
)
combined_svm.fit(X_train_combined, y_train)
y_combined = combined_svm.predict(X_val_combined)
y_combined_score = combined_svm.decision_function(X_val_combined)
print(f"\nAccuracy: {accuracy_score(y_val, y_combined)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_combined)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_combined_score)}")
print(f"\nClassification report:\n{classification_report(y_val, y_combined, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_combined)}")
# Accuracy: 0.8383394383394384
# Balanced accuracy: 0.830007130812702
# ROC_AUC Score: 0.9145666439584238
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.85      0.88      0.86      2377
#            1       0.83      0.78      0.80      1718
# 
#     accuracy                           0.84      4095
#    macro avg       0.84      0.83      0.83      4095
# weighted avg       0.84      0.84      0.84      4095
# 
# Confusion Matrix:
# [[2096  281]
#  [ 381 1337]]
## }}}

## {{{ raw extracted AST tokens encoded by TF-IDF 
##
import ast

source = '''
def calculate(x):
  if x > 0:
    return process(x)
  return 0
'''

class ASTTokenExtractor(ast.NodeVisitor):
  def __init__(self):
    self.tokens = []

  def generic_visit(self, node):
    self.tokens.append(type(node).__name__)
    super().generic_visit(node)

def extract_features(source):
  tree = ast.parse(source)
  extractor = ASTTokenExtractor()
  extractor.visit(tree)
  return " ".join(extractor.tokens)

features = extract_features(source)
print(features)
# Module FunctionDef arguments arg If Compare Name Load Gt Constant Return Call Name Load Name Load Return Constant
## 

## 
train_X = train["source_code"].apply(extract_features)
val_X = val["source_code"].apply(extract_features)
print(train_X.iloc[0])
# Module FunctionDef arguments arg arg Assign Name Store Constant Assign Name Store Call Name Load keyword Constant keyword Attribute Name Load Load keyword JoinedStr Constant FormattedValue Name Load Constant FormattedValue Attribute Name Load Load keyword Constant keyword Attribute Name Load Load Assert Compare Name Load IsNot Constant Expr Call Attribute Name Load Load Constant Assign Name Store Call Name Load keyword Constant Assign Name Store Call Attribute Name Load Load Constant Expr Call Attribute Name Load Load keyword Attribute Name Load Load Assert Call Attribute Name Load Load Attribute Name Load Load Assign Name Store Call Name Load keyword Name Load keyword Name Load keyword Name Load keyword Name Load keyword Name Load keyword Name Load keyword Constant keyword Attribute Name Load Load Assert Compare Name Load IsNot Constant Expr Call Attribute Name Load Load Constant Assign Name Store Call Attribute Name Load Load keyword Attribute Name Load Load keyword Attribute Name Load Load Assert Compare Call Name Load Subscript Name Load Constant Load Eq Constant Assert Compare Subscript Subscript Subscript Name Load Constant Load Constant Load Constant Load Eq Attribute Name Load Load Expr Call Attribute Name Load Load keyword Attribute Name Load Load keyword Attribute Name Load Load Expr Call Attribute Name Load Load keyword Attribute Name Load Load Assert UnaryOp Not Call Attribute Name Load Load Attribute Name Load Load

vectorizer = TfidfVectorizer(
  ngram_range=(1, 3),
)

train_X = vectorizer.fit_transform(train_X)
val_X = vectorizer.transform(val_X)
svm = LinearSVC(
  C=10.0,
  random_state=SEED,
  max_iter=2000,
)

svm.fit(train_X, y_train)
y_pred = svm.predict(val_X)
y_score = svm.decision_function(val_X)
print(f"\nAccuracy: {accuracy_score(y_val, y_pred)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_pred)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_score)}")
print(f"\nClassification report:\n{classification_report(y_val, y_pred, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")
# Accuracy: 0.8588522588522588
# Balanced accuracy: 0.8498550084409036
# ROC_AUC Score: 0.9229354313725393
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.86      0.91      0.88      2377
#            1       0.86      0.79      0.83      1718
# 
#     accuracy                           0.86      4095
#    macro avg       0.86      0.85      0.85      4095
# weighted avg       0.86      0.86      0.86      4095
# 
# Confusion Matrix:
# [[2153  224]
#  [ 354 1364]]
# 
##
## }}}

## Combine TF-IDF AST tokens with TF-IDF source-code tokens
from scipy.sparse import hstack, csr_matrix

X_train_combined = hstack([
  X_train_tfidf,
  train_X,
])

X_val_combined = hstack([
  X_val_tfidf,
  val_X,
])

svc = LinearSVC(
  C=10.0,
  max_iter=2000,
  random_state=SEED,
)

svc.fit(X_train_combined, y_train)
y_combined = svc.predict(X_val_combined)
y_combined_score = svc.decision_function(X_val_combined)
print(f"\nAccuracy: {accuracy_score(y_val, y_combined)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_val, y_combined)}")
print(f"ROC_AUC Score: {roc_auc_score(y_val, y_combined_score)}")
print(f"\nClassification report:\n{classification_report(y_val, y_combined, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_val, y_combined)}")
# Accuracy: 0.8783882783882784
# Balanced accuracy: 0.8674091249914906
# ROC_AUC Score: 0.9451475945995848
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.87      0.94      0.90      2377
#            1       0.90      0.80      0.85      1718
# 
#     accuracy                           0.88      4095
#    macro avg       0.88      0.87      0.87      4095
# weighted avg       0.88      0.88      0.88      4095
# 
# Confusion Matrix:
# [[2224  153]
#  [ 345 1373]]
# 

## {{{ final training and testing
X_train_val_tfidf = best_model.named_steps["tfidf"].transform(train_val["source_code"])
X_test_tfidf = best_model.named_steps["tfidf"].transform(test["source_code"])
X_train_val_tokens = vectorizer.transform(train_val["source_code"].apply(extract_features))
X_test_tokens = vectorizer.transform(test["source_code"].apply(extract_features))
X_train_val_combined = hstack([
  X_train_val_tfidf,
  X_train_val_tokens,
])
y_train_val = train_val["is_vulnerable"].values
X_test_combined = hstack([
  X_test_tfidf,
  X_test_tokens,
])
y_test = test["is_vulnerable"].values
svc = LinearSVC(
  C=10.0,
  max_iter=2000,
  random_state=SEED,
)
svc.fit(X_train_val_combined, y_train_val)
y_combined = svc.predict(X_test_combined)
y_combined_score = svc.decision_function(X_test_combined)
print(f"\nAccuracy: {accuracy_score(y_test, y_combined)}")
print(f"Balanced accuracy: {balanced_accuracy_score(y_test, y_combined)}")
print(f"ROC_AUC Score: {roc_auc_score(y_test, y_combined_score)}")
print(f"\nClassification report:\n{classification_report(y_test, y_combined, zero_division=0)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_combined)}")
# Accuracy: 0.7773769646998197
# Balanced accuracy: 0.6908185943953147
# ROC_AUC Score: 0.8701536505121683
# 
# Classification report:
#               precision    recall  f1-score   support
# 
#            0       0.75      0.98      0.85      2521
#            1       0.92      0.40      0.56      1360
# 
#     accuracy                           0.78      3881
#    macro avg       0.83      0.69      0.70      3881
# weighted avg       0.81      0.78      0.75      3881
# 
# Confusion Matrix:
# [[2471   50]
#  [ 814  546]]
# 
# why??? 😭😭😭
## }}}
## {{{ investigating 🧐
print("Source vocabulary:", len(best_model.named_steps["tfidf"].vocabulary_))
print("AST vocabulary:", len(vectorizer.vocabulary_))

print("Train + validation:", len(train_val))
print("Test:", len(test))

print("Train + validation labels:")
print(train_val["is_vulnerable"].value_counts(normalize=True))

print("Test labels:")
print(test["is_vulnerable"].value_counts(normalize=True))
# Source vocabulary: 455333
# AST vocabulary: 5585
# Train + validation: 13811
# Test: 3881
# Train + validation labels:
# is_vulnerable
# 0    0.532112
# 1    0.467888
# Name: proportion, dtype: float64
# Test labels:
# is_vulnerable
# 0    0.649575
# 1    0.350425
# Name: proportion, dtype: float64
## }}}
## }}}
