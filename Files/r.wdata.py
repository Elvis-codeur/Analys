ANALYS-file-version-2
<data>
0,370,817,853
1,405,1023,851
2,211,1420,967
3,149,827,942
4,539,633,885
5,373,343,734
6,342,194,697
7,75,435,883
8,598,914,1024
9,497,869,715
10,569,390,1014
</data>
<code>
<script>
import matplotlib.pyplot as plt
def courant_rl_serie(R,L,Y,I_0,t):
    """ R: La rÃ©sistance
        L: Inductance
        Y: La seconde partie de l'Ã©quation diffÃ©rentielle
        t: le temps
    """
    
    return (I_0-Y)*np.exp(-t*(R/L)) + Y/R
</script>
<script>
R = 220
L = 0.1
Y = 0
I_0 = 1


a = np.arange(0,0.004,0.0001)
b = []
for i in range(len(a)):
    b.append(courant_rl_serie(R,L,Y,I_0,a[i]))


print(max(a))
print(len(a))
#plt.yscale("log")
plt.plot(a,b)
plt.show()
</script>

</code>