template <typename T1, typename T2>
MOBULA_KERNEL some_op_kernel(const int n, const T1* a, const T2* b, T1* c) {
  parfor(n, [&](int i) {
    c[i] = a[i] + static_cast<T1>(b[i]);
  });
}
