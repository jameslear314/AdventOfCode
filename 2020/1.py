DATA = [176, 256, 401, 671, 703, 874, 890, 892, 980, 1062, 1103, 1128, 1144, 1169, 1185, 1210, 1288, 1309, 1314, 1320, 1330, 1343, 1344, 1359, 1360, 1372, 1393, 1394, 1406, 
1407, 1408, 1412, 1413, 1416, 1418, 1423, 1425, 1426, 1429, 1456, 1463, 1470, 1471, 1472, 1473, 1475, 1477, 1481, 1484, 1486, 1487, 1491, 1493, 1494, 1496, 1502, 1504, 1505, 1511, 1512, 1517, 1518, 1520, 1521, 1527, 1530, 1532, 1533, 1535, 1536, 1539, 1541, 1544, 1545, 1548, 1551, 1555, 1556, 1560, 1563, 1566, 1568, 1569, 1573, 1589, 1593, 1595, 1610, 1611, 1612, 1626, 1627, 1629, 1632, 1636, 1642, 1663, 1667, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1689, 1690, 1692, 1693, 1694, 
1697, 1699, 1700, 1705, 1706, 1709, 1711, 1716, 1721, 1729, 1730, 1736, 1738, 1740, 1743, 1750, 1757, 1758, 1760, 1762, 1763, 1766, 1767, 1770, 1772, 1780, 1783, 1784, 1811, 1815, 1816, 1819, 1825, 1827, 1829, 1831, 1832, 1834, 1835, 1841, 1847, 1850, 1854, 1861, 1862, 1866, 1869, 1870, 1871, 1875, 1878, 1880, 1887, 1890, 1891, 1894, 1896, 1897, 1899, 1901, 1903, 1908, 1914, 1919, 1924, 1932, 1937, 1944, 1957, 1958, 1959, 1963, 1964, 1965, 1967, 1970, 1971, 1973, 1979, 1980, 1982, 1983, 1989, 
1990, 1998, 1999, 2000, 2005]

def solve():
    for i in DATA:
        for j in DATA:
            if i + j == 2020:
                print(i, j)
                print(i * j)

def multiply():
    answer = 241861950
    for i in DATA:
        for j in DATA:
            residual = 2020 - i - j
            if residual in DATA:
                print(i * j * residual)




if __name__ == '__main__':
    # solve()
    multiply()