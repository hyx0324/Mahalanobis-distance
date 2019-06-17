# Mahalanobis-distance
My friend ask me to help him deel with some datas using Mahalanobis-distance method.  
I record this process.
## Specific Example
We have N datas.  
When the number of data (index=i) < 7, we need fill up to 7.  
Let ni represent the data of which index=i (ni<7)  
We need to calculate Mahalanobis-distance of the data except data of which index=i  
<a href="https://www.codecogs.com/eqnedit.php?latex=W_{m}=\frac{1}{n_{i}}\sum_{k=1}^{n_{i}}\frac{1}{7}\sum_{j=1}^{7}A_{ij}\beta&space;_{kj}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?W_{m}=\frac{1}{n_{i}}\sum_{k=1}^{n_{i}}\frac{1}{7}\sum_{j=1}^{7}A_{ij}\beta&space;_{kj}" title="W_{m}=\frac{1}{n_{i}}\sum_{k=1}^{n_{i}}\frac{1}{7}\sum_{j=1}^{7}A_{ij}\beta _{kj}" /></a>  
m=N-ni  
β means the data of which index=i, A means other datas.  
We then find the largest (7-ni) of Wm, and fill up the Am.
