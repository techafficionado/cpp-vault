import json
import sys
import re
import pprint

if __name__ == "__main__":
	pp = pprint.PrettyPrinter(indent=4)
	gtgrids = {}
	matVals = []
	matstart = False
	with open('GTGridFiles/GT_Grids.txt', 'r') as gtGridFile:
		for line in gtGridFile:
			#print "line1:"+str(line)
			#print "line strip:"+str(line.strip())
			while line.strip():
				#print "line in while:"+str(line)
				if "Name" in line:
					netName = (re.findall('Name: (.*)', line)[0]).strip()
					print "netName:"+str(netName)
					break
				if "satLongitude: " in line:
					satlong = re.findall('satLongitude: (.*)', line)[0]
					st = {"satlong":satlong}
					break
				if "lat_grid_deg: " in line:
					lat_grid_deg = re.findall('lat_grid_deg: (.*)', line)[0]
					lat_grid_deg_list = lat_grid_deg.split()
					latgg = {"lat_grid_deg":lat_grid_deg_list}
					break
				if "lon_grid_deg: " in line:
					lon_grid_deg = re.findall('lon_grid_deg: (.*)', line)[0]
					lon_grid_deg_list = lon_grid_deg.split()
					longg = {"lon_grid_deg":lon_grid_deg_list}
					break
				if "maxGridValue: " in line:
					maxgain = re.findall('maxGridValue: (.*)', line)[0]
					maxg = {"maxgain":maxgain}
					break
				if "minGridValue: " in line:
					mingain = re.findall('minGridValue: (.*)', line)[0]
					ming = {"mingain":mingain}
					break
				if "minLon_deg: " in line:
					minLon_deg = re.findall('minLon_deg: (.*)', line)[0]
					mlond = {"minLon_deg":minLon_deg}
					break
				if "minLat_deg: " in line:
					minLat_deg = re.findall('minLat_deg: (.*)', line)[0]
					mlatd = {"minLat_deg":minLat_deg}
					break
				if "deltaLon_deg: " in line:
					deltaLon_deg = re.findall('deltaLon_deg: (.*)', line)[0]
					dlond = {"deltaLon_deg":deltaLon_deg}
					break
				if "deltaLat_deg: " in line:
					deltaLat_deg = re.findall('deltaLat_deg: (.*)', line)[0]
					dlatd = {"deltaLat_deg":deltaLat_deg}
					matstart = True
					break
					#continue
				if matstart:
					print "in matstart"
					matValsRow = line.split()
					#msg = "matValsRow:"+str(matValsRow)
					#log(msg, True)
					matVals.append(matValsRow)
					break
					# check for blank new line
			if not line.strip():
				print "in matstart line strip"
				matstart = False
				#print "Building netParams"
				#netParams = [satlong, lat_grid_deg, lon_grid_deg, maxgain, mingain, minLon_deg, minLat_deg, deltaLon_deg, deltaLat_deg, matVals]
				netParams =  {"satlong": satlong.strip(), #0
						"lat_grid_deg":lat_grid_deg_list, #1
						"lon_grid_deg":lon_grid_deg_list, #2
						"maxgain":maxgain.strip(), #3
						"mingain":mingain.strip(), #4
						"minLon_deg":minLon_deg.strip(), #5
						"minLat_deg":minLat_deg.strip(), #6
						"deltaLon_deg":deltaLon_deg.strip(), #7
						"deltaLat_deg":deltaLat_deg.strip(),#8
						"gtVals": matVals} #9
						
				#if netName in gtgrids.keys():
				#	gtgrids[netName].append(netParams)
				#else:
				gtgrids[netName] = netParams
				#print "continuing"
				matVals = [] #empty the list
				print "gtgrid for net: "+str(netName)+" is:"+str(gtgrids[netName])
				continue 

	gtGridFile.close()		
	#print "Network Data added:"#str(gtgrids)
	print "gtgrids:"+str(gtgrids)
	#pp.pprint(gtgrids)
	with open('GTGridVals.json','w') as outFile:
		print(str(json.dump(gtgrids,outFile)))

	outFile.close()
	#print "satlong for MTNPAC_IS29e_U5_T01"+str(gtgrids['MTNPAC_IS29e_U5_T01']['satlong'])
	#print "lat_grid_deg for MTNPAC_IS29e_U5_T01"+str(gtgrids['MTNPAC_IS29e_U5_T01']['lat_grid_deg'])
	#print "lon_grid_deg for MTNPAC_IS29e_U5_T01"+str(gtgrids['MTNPAC_IS29e_U5_T01']['lon_grid_deg'])
	#print "gtloc value for MTNPAC_GE23SP_T01"+str(gtgrids['MTNPAC_GE23SP_T01']['gtVals'])#[16][1])

