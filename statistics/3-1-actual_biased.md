[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> ```python 
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)
import thinkplot
thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()
def BiasPmf(pmf, label=''):
  new_pmf = pmf.Copy(label=label)
  for x, p in pmf.Items():
    new_pmf.Mult(x, x)
  new_pmf.Normalize()
  return new_pmf
biased = BiasPmf(pmf, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()
```
