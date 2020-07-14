import arcpy
import pythonaddins

# reset to current .mxd
emexd = arcpy.mapping.MapDocument('current')
# assign all layers in current .mxd to a variable array    
layers = arcpy.mapping.ListLayers(emexd)

selattrib = "Select Attribute"

emexditems = []
emexdattrib = {}
emexdalias = {}
emexdflds = []

featclasses = emexditems
# iterate across every layer in Table of Contents
for df in arcpy.mapping.ListDataFrames(emexd):
	# print str(df.name)
	try:
		dflayers = arcpy.mapping.ListLayers(df)
		# print str(dflayers)
		for layer in dflayers:
			if layer.name not in emexditems:
				emexditems.append(layer.name)
			emexditems.sort()
			try:
				fields = arcpy.ListFields(layer)
				for field in fields:
					# print(field.name)
					# get field name
					fldnam = ("{0}"
						.format(field.name))
					# get field type
					fldtyp = ("{0}"
						.format(field.type))
					#get field alias
					fldals = ("{0}"
						.format(field.aliasName))
					try:
						# update the attribute FIELDNAME : TYPE dictionary
						emexdattrib[fldnam] = fldtyp
						# update the attribute FIELDNAME : FIELDALIAS dictionary
						emexdalias[fldnam] = fldals
						# update the FIELDALIAS array
						if fldals not in emexdflds:
							emexdflds.append(fldals)
						emexdflds.sort()
					except:
						print "Couldn't update " + fldnam
					# if field.name not in emexdflds:
						# emexdflds.append(field.name)
					# emexdflds.sort()
			except:
				for layer in dflayers:
					try:
						grouplayers = arcpy.mapping.ListLayers(layer)
						for grouplayer in grouplayers:
							if grouplayer.name not in emexditems:
								emexditems.append(grouplayer.name)
							emexditems.sort()
							try:
								glfields = arcpy.ListFields(grouplayer)
								for glfield in glfields:
									# print(glfield.name)
									# get field name
									fldnam = ("{0}"
										.format(field.name))
									# get field type
									fldtyp = ("{0}"
										.format(field.type))
									#get field alias
									fldals = ("{0}"
										.format(field.aliasName))
									try:
										# update the attribute FIELDNAME : TYPE dictionary
										emexdattrib[fldnam] = fldtyp
										# update the attribute FIELDNAME : FIELDALIAS dictionary
										emexdalias[fldnam] = fldals
										# update the FIELDALIAS array
										if fldals not in emexdflds:
											emexdflds.append(fldals)
										emexdflds.sort()
									except:
										print "Couldn't update " + fldnam
									# if glfield.name not in emexdflds:
										# emexdflds.append(glfield.name)
									# emexdflds.sort()

							except:
								for grouplayer in grouplayers:
									try:
										subgrouplayers = arcpy.mapping.ListLayers(grouplayer)
										for subgrouplayer in subgrouplayers:
											if subgrouplayer.name not in emexditems:
												emexditems.append(subgrouplayer.name)
											emexditems.sort()
											try:
												sglfields = arcpy.ListFields(subgrouplayer)
												for sglfield in sglfields:
													# print(sglfield.name)
													# get field name
													fldnam = ("{0}"
														.format(field.name))
													# get field type
													fldtyp = ("{0}"
														.format(field.type))
													#get field alias
													fldals = ("{0}"
														.format(field.aliasName))
													try:
														# update the attribute FIELDNAME : TYPE dictionary
														emexdattrib[fldnam] = fldtyp
														# update the attribute FIELDNAME : FIELDALIAS dictionary
														emexdalias[fldnam] = fldals
														# update the FIELDALIAS array
														if fldals not in emexdflds:
															emexdflds.append(fldals)
														emexdflds.sort()
													except:
														print "Couldn't update " + fldnam
													# if sglfield.name not in emexdflds:
														# emexdflds.append(sglfield.name)
													# emexdflds.sort()
											except:
												for subgrouplayer in subgrouplayers:
													try:
														supsubgrouplayers = arcpy.mapping.ListLayers(subgrouplayer)
														for supsubgrouplayer in supsubgrouplayers:
															if supsubgrouplayer.name not in emexditems:
																emexditems.append(subgrouplayer.name)
															emexditems.sort()
															try:
																ssglfields = arcpy.ListFields(supsubgrouplayer)
																for ssglfield in ssglfields:
																	# print(ssglfield.name)
																	# get field name
																	fldnam = ("{0}"
																		.format(field.name))
																	# get field type
																	fldtyp = ("{0}"
																		.format(field.type))
																	#get field alias
																	fldals = ("{0}"
																		.format(field.aliasName))
																	try:
																		# update the attribute FIELDNAME : TYPE dictionary
																		emexdattrib[fldnam] = fldtyp
																		# update the attribute FIELDNAME : FIELDALIAS dictionary
																		emexdalias[fldnam] = fldals
																		# update the FIELDALIAS array
																		if fldals not in emexdflds:
																			emexdflds.append(fldals)
																		emexdflds.sort()
																	except:
																		print "Couldn't update " + fldnam
																	# if ssglfield.name not in emexdflds:
																		# emexdflds.append(ssglfield.name)
																	# emexdflds.sort()
															except:
																print supsubgrouplayer + " did not have fields."
													except:
														print subgrouplayer + " did not have fields."
									except:
										print grouplayer + " did not have fields."
					except:
						print str(layer.name) + " did not have fields."
	except:
		print str(df.name) + " was not included."
print(emexdflds)
print(emexditems)

class AttributeComboBoxClass2(object):
	global emexdflds
	selattrib = "Select Attribute"
	def __init__(self):
		self.items = emexdflds
		self.editable = True
		self.enabled = True
		self.dropdownWidth = 'WWWWWWWW'
		self.width = 'WWWWWWWW'
	def onSelChange(self, selection):
		self.items = emexdflds
		global selattrib
		selattrib = selection
	def onEditChange(self, text):
		self.items = emexdflds
		global selattrib
		selattrib = text
	def onFocus(self, focused):
		self.items = emexdflds
		global selattrib
	def onEnter(self):
		global selattrib
	def refresh(self):
		self.items = emexdflds
		global emexdflds

class ReloadButtonClass1(object):
	global emexd
	# reset to current .mxd
	emexd = arcpy.mapping.MapDocument('current')
	# assign all layers in current .mxd to a variable array
	layers = arcpy.mapping.ListLayers(emexd)
	"""Implementation for FastSearchReload_addin.button (Button)"""
	def __init__(self):
		self.enabled = True
		self.checked = False
	def onClick(self):
		global emexd
		# reset to current .mxd
		emexd = arcpy.mapping.MapDocument('current')
		# assign all layers in current .mxd to a variable array
		layers = arcpy.mapping.ListLayers(emexd)
		# reset arrays and dictionaries to empty sets
		global emexditems
		#del emexditems
		emexditems = []
		global emexdattrib
		#del emexdattrib
		emexdattrib = {}
		global emexdalias
		#del emexdalias
		emexdalias = {}
		global emexdflds
		#del emexdflds
		emexdflds = []
		# iterate across every layer in Table of Contents
		for df in arcpy.mapping.ListDataFrames(emexd):
			# print str(df.name)
			try:
				dflayers = arcpy.mapping.ListLayers(df)
				# print str(dflayers)
				for layer in dflayers:
					if layer.name not in emexditems:
						emexditems.append(layer.name)
					emexditems.sort()
					try:
						fields = arcpy.ListFields(layer)
						for field in fields:
							# print(field.name)
							# get field name
							fldnam = ("{0}"
								.format(field.name))
							# get field type
							fldtyp = ("{0}"
								.format(field.type))
							#get field alias
							fldals = ("{0}"
								.format(field.aliasName))
							try:
								# update the attribute FIELDNAME : TYPE dictionary
								emexdattrib[fldnam] = fldtyp
								# update the attribute FIELDNAME : FIELDALIAS dictionary
								emexdalias[fldnam] = fldals
								# update the FIELDALIAS array
								if fldals not in emexdflds:
									emexdflds.append(fldals)
								emexdflds.sort()
							except:
								print "Couldn't update " + fldnam
							# if field.name not in emexdflds:
								# emexdflds.append(field.name)
							# emexdflds.sort()
					except:
						for layer in dflayers:
							try:
								grouplayers = arcpy.mapping.ListLayers(layer)
								for grouplayer in grouplayers:
									if grouplayer.name not in emexditems:
										emexditems.append(grouplayer.name)
									emexditems.sort()
									try:
										glfields = arcpy.ListFields(grouplayer)
										for glfield in glfields:
											# print(glfield.name)
											# get field name
											fldnam = ("{0}"
												.format(field.name))
											# get field type
											fldtyp = ("{0}"
												.format(field.type))
											#get field alias
											fldals = ("{0}"
												.format(field.aliasName))
											try:
												# update the attribute FIELDNAME : TYPE dictionary
												emexdattrib[fldnam] = fldtyp
												# update the attribute FIELDNAME : FIELDALIAS dictionary
												emexdalias[fldnam] = fldals
												# update the FIELDALIAS array
												if fldals not in emexdflds:
													emexdflds.append(fldals)
												emexdflds.sort()
											except:
												print "Couldn't update " + fldnam
											# if glfield.name not in emexdflds:
												# emexdflds.append(glfield.name)
											# emexdflds.sort()

									except:
										for grouplayer in grouplayers:
											try:
												subgrouplayers = arcpy.mapping.ListLayers(grouplayer)
												for subgrouplayer in subgrouplayers:
													if subgrouplayer.name not in emexditems:
														emexditems.append(subgrouplayer.name)
													emexditems.sort()
													try:
														sglfields = arcpy.ListFields(subgrouplayer)
														for sglfield in sglfields:
															# print(sglfield.name)
															# get field name
															fldnam = ("{0}"
																.format(field.name))
															# get field type
															fldtyp = ("{0}"
																.format(field.type))
															#get field alias
															fldals = ("{0}"
																.format(field.aliasName))
															try:
																# update the attribute FIELDNAME : TYPE dictionary
																emexdattrib[fldnam] = fldtyp
																# update the attribute FIELDNAME : FIELDALIAS dictionary
																emexdalias[fldnam] = fldals
																# update the FIELDALIAS array
																if fldals not in emexdflds:
																	emexdflds.append(fldals)
																emexdflds.sort()
															except:
																print "Couldn't update " + fldnam
															# if sglfield.name not in emexdflds:
																# emexdflds.append(sglfield.name)
															# emexdflds.sort()
													except:
														for subgrouplayer in subgrouplayers:
															try:
																supsubgrouplayers = arcpy.mapping.ListLayers(subgrouplayer)
																for supsubgrouplayer in supsubgrouplayers:
																	if supsubgrouplayer.name not in emexditems:
																		emexditems.append(subgrouplayer.name)
																	emexditems.sort()
																	try:
																		ssglfields = arcpy.ListFields(supsubgrouplayer)
																		for ssglfield in ssglfields:
																			# print(ssglfield.name)
																			# get field name
																			fldnam = ("{0}"
																				.format(field.name))
																			# get field type
																			fldtyp = ("{0}"
																				.format(field.type))
																			#get field alias
																			fldals = ("{0}"
																				.format(field.aliasName))
																			try:
																				# update the attribute FIELDNAME : TYPE dictionary
																				emexdattrib[fldnam] = fldtyp
																				# update the attribute FIELDNAME : FIELDALIAS dictionary
																				emexdalias[fldnam] = fldals
																				# update the FIELDALIAS array
																				if fldals not in emexdflds:
																					emexdflds.append(fldals)
																				emexdflds.sort()
																			except:
																				print "Couldn't update " + fldnam
																			# if ssglfield.name not in emexdflds:
																				# emexdflds.append(ssglfield.name)
																			# emexdflds.sort()
																	except:
																		print supsubgrouplayer + " did not have fields."
															except:
																print subgrouplayer + " did not have fields."
											except:
												print grouplayer + " did not have fields."
							except:
								print str(layer.name) + " did not have fields."
			except:
				print str(df.name) + " was not included."

		print(emexdflds)
		global emexdflds
		print(emexditems)
		global emexditems
					
class SearchButtonClass4(object):
	global emexditems
	global featclasses
	global selattrib
	global ProjectName
	featclasses = emexditems
	arcpy.SetLogHistory(False)
	def __init__(self):
		self.enabled = True
		self.checked = False
	def onClick(self):
		featclasses = emexditems
		for fc in featclasses:
			SAS_Stormwater_SDE_swManhole = fc
			try:
				arcpy.SelectLayerByAttribute_management(SAS_Stormwater_SDE_swManhole, "NEW_SELECTION", selattrib + " LIKE '%" + ProjectName + "%'")
			except:
				print " Skip " + fc
			del SAS_Stormwater_SDE_swManhole
	arcpy.SetLogHistory(True)

class SearchComboBoxClass3(object):
	global emexditems
	global featclasses
	global selattrib
	global ProjectName
	featclasses = emexditems
	arcpy.SetLogHistory(False)
	def __init__(self):
		self.items = []
		self.editable = True
		self.enabled = True
		self.dropdownWidth = 'WWWWWWW'
		self.width = 'WWWWWWW'
	def onSelChange(self, selection):
		pass
	def onEditChange(self, text):
		global ProjectName
		ProjectName = text
	def onFocus(self, focused):
		pass
	def onEnter(self):
		featclasses = emexditems
		for fc in featclasses:
			SAS_Stormwater_SDE_swManhole = fc
			try:
				arcpy.SelectLayerByAttribute_management(SAS_Stormwater_SDE_swManhole, "NEW_SELECTION", selattrib + " LIKE '%" + ProjectName + "%'")
			except:
				print " Skip " + fc
			del SAS_Stormwater_SDE_swManhole
	def refresh(self):
		pass
	arcpy.SetLogHistory(True)