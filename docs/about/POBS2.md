#POBS 0.0.1
# kitty-cat
`is`
black[^1]  
nice[^1] 
fun[^1] 
cool[^1]

`has` [hat](#hat)[^1]

`used-for` companionship[^2]
# hat
`is` blue[^1]

[^1]: catinfo.com
[^2]: lies.com

  
#POBS 0.0.2

``` definition
time format: (`<YYYY-MM-DDTHH:mm:ss.SSS`)
```

# kitty-cat

`is`
black[^1](`t>:2024`)[^1]
nice[^1] 
fun[^1] 
cool[^1](`if:happy`)
happy[^3](`)

`was` 
cool[^1](`t<:2022`)[^1]

`has` [hat]()[^1]

`had` mittens[^1](`t<:2022`)[^1]

`used-for` companionship[^2]


[^1]: catinfo.com
[^2]: lies.com
[^3]: kitty-schedule.com


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 


# Landsat-Program
`is` a joint initiative[^1] 
a long-running Earth observation program[^1] 
critical for monitoring global environmental change[^2]

`developedBy` [NASA](https://www.nasa.gov/)[^1] 
[USGS](https://www.usgs.gov/)[^1]

`status` operational (as of April 2025)[^3]

`launched`
`^if` A
`^then` Landsat 1 (ERTS-1): 1972[^1] 
Landsat 8: 2013[^4] 
Landsat 9: 2021[^5]

`provides` continuous global imagery[^1] 
multispectral data[^4] 
thermal data[^4] 
a basis for [Analysis Ready Data (ARD)](https://www.usgs.gov/landsat-missions/landsat-analysis-ready-data)[^6]

`hasSensor` OLI (Operational Land Imager) (on Landsat 8, 9)[^4][^5] 
TIRS (Thermal Infrared Sensor) (on Landsat 8, 9)[^4][^5] 
MSS (Multispectral Scanner) (on Landsat 1-5)[^1] 
TM (Thematic Mapper) (on Landsat 4, 5)[^1] 
ETM+ (Enhanced Thematic Mapper Plus) (on Landsat 7)[^7]

`resolution` 30m (multispectral)[^4] 
100m (thermal, resampled to 30m)[^4] 
15m (panchromatic, Landsat 7, 8, 9)[^4][^5][^7]

`swathWidth` 185 km[^4]

`repeatCycle` 16 days (Landsat 7, 8, 9)[^3][^4][^5] 
8 days (combined Landsat 8 and 9)[^5]

`dataPolicy` Free and open access (since 2008)[^8]

`usedFor` Agriculture monitoring[^2] 
Forestry studies[^2][^9] 
Water resource management[^2] 
Urban growth analysis[^10] 
Disaster response (e.g., floods, fires)[^11] 
Climate change research[^2] 
Land cover mapping[^9]

`status:Landsat7` Operational but with Scan Line Corrector (SLC) failure (since 2003)[^7]

`requires` Ground stations for data downlink and processing[^1] 
Calibration and validation activities (e.g., RadCalNet)[^12]

`influencedBy` Technological advancements in sensors[^4] 
Evolving user needs for data quality and frequency[^6] 
Budget allocations and policy decisions[^1]

`website` [USGS Landsat Missions](https://www.usgs.gov/landsat-missions)[^1]


[^1]: Overview of the Landsat Program History. *USGS Publications*, 2018.
[^2]: Goward, S. L., et al. "The Landsat legacy: A global perspective." *Remote Sensing of Environment*, vol. 105, no. 3, 2006, pp. 173-176.
[^3]: Personal Communication, USGS Landsat Team, April 2025. (Hypothetical source for current status)
[^4]: Irons, J. R., et al. "The next Landsat satellite: The Landsat Data Continuity Mission." *Remote Sensing of Environment*, vol. 122, 2012, pp. 11-21. (Describes Landsat 8)
[^5]: Markham, B.L., et al. "Landsat 9: Mission Overview and Status." *IGARSS 2022*.
[^6]: Dwyer, J. L., et al. "Analysis Ready Data: Enabling analysis of the Landsat archive." *Remote Sensing*, vol. 10, no. 9, 2018, p. 1363.
[^7]: Landsat 7 Science Data Users Handbook. *NASA/USGS*, Updated 2020.
[^8]: Woodcock, C. E., et al. "Free access to Landsat imagery." *Science*, vol. 320, no. 5879, 2008, p. 1011.
[^9]: Cohen, W. B., & Goward, S. N. "Landsat's role in ecological applications of remote sensing." *BioScience*, vol. 54, no. 6, 2004, pp. 535-545.
[^10]: Schneider, A., et al. "A global map of urban extent from MODIS data." *Remote Sensing of Environment*, vol. 113, no. 9, 2009, pp. 1941-1947. (Often uses Landsat for validation/finer scale)
[^11]: Landsat Applications in Disaster Management. *NASA Earth Observatory*.
[^12]: RadCalNet: Radiometric Calibration Network Portal. *ESA/NASA*.