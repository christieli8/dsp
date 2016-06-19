[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
```python
import thinkstats2
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
cdf = thinkstats2.Cdf(live.totalwgt_lb)
import thinkplot
thinkplot.Cdf(cdf, label='totalwgt_lb')
thinkplot.Show(loc='lower right')
cdf.Prob(6.4)
other_cdf = thinkstats2.Cdf(others.totalwgt_lb)
other_cdf.Prob(6.4)
cdf.PercentileRank(6.4)
```

