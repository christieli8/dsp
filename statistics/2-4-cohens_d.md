[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> ```python 
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
```

```python 
def WeightDifference(live, firsts, others):
    #live: DataFrame of all live births
    firsts: DataFrame of first babies
    others: DataFrame of others
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()
    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()
    print('Mean')
    print('First babies', mean1)
    print('Others', mean2)
    print('Variance')
    print('First babies', var1)
    print('Others', var2)
    print('Difference in lbs', mean1 - mean2)
    print('Difference in oz', (mean1 - mean2) * 16)
    print('Difference relative to mean (%age points)', 
          (mean1 - mean2) / mean0 * 100)
d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)
```

The Cohen's efficient mearsures the size effect of the difference in means of first births and other babies. 
