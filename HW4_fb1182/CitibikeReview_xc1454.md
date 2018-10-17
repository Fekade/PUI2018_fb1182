# Comments

a. I already email Fekade to make sure I understand his hypothesis correctly. Here he want to know if there more students dock the bike in the stations near high schools than other stations. So he assumes people age from 16-18 are high school students and the time from 7:55 am to 8:30 am is the time that students go to high schools. Here he will assign some stations near high schools named End Station Name A. 

But here, it would be little arbitrary to assume people age from 16-18 is high school student. This data will be dirty and the result do not convictive. What's more, the time which assume as students go to high school should be tested or verified by other datas or resources.


The formula could be better if change into the formula below. As the number of Other End Station and the number of End Station Name A maybe not equal, we should to use the average to make the test more fair. 

_$H_0$ : $\frac{Children(16,18)\_{\mathrm{Other End Station Names}}}{{\mathrm{OtherEndStation\_Num}}} <= \frac{Children(16,18)\_{\mathrm{End Station Name A}}}{{\mathrm{EndStationNameA_Num}}}$
    
_$H_1$ : $\frac{Children(16,18)\_{\mathrm{Other End Station Names}}}{{\mathrm{OtherEndStation\_Num}}} > \frac{Children(16,18)\_{\mathrm{End Station Name A}}}{{\mathrm{EndStationNameA_Num}}}$


b. About the support data, I think you should not only test the NAN of data, but also calculate the age of each rider and filter the age from 16 to 18, then filter the stoptime from 7:55 am to 8:30 am. Then count the number of children docking the bike in End Station Name A and Other End Station each day in 01.2016. 

c. As we do not have much data, the data may not follow Gaussian distribution. And the two groups are parallel and independent groups, so we should use Mann–Whitney U test (Wilcoxon rank-sum test) to do this test.