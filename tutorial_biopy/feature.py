# Section 4.3
# Feature, location, position objects

from Bio import SeqFeature
from Bio import SeqIO

def main():

	print(50 * '-')
	print('Start position')
	start_pos = SeqFeature.AfterPosition(109)
	print(start_pos)
	
	print(50 * '-')
	print('End position')	
	end_pos = SeqFeature.WithinPosition(689, left=667, right=689)
	print(end_pos)

	print(50 * '-')
	print('Location')
	location = SeqFeature.SimpleLocation(start_pos, end_pos)
	print(location)

	print(50 * '-')
	print('Load a GenBank file')
	record = SeqIO.read('io/yersinia_pestis.gb', "genbank")

	print(50 * '-')
	print('Inspecting the record')
	print(record.name)

	print(50 * '-')
	print('Record ID')
	print(record.id)

	print(50 * '-')
	print('Record\'s description')
	print(record.description)

	print(50 * '-')
	print('Source')
	print(record.annotations['source'])

	print(50 * '-')
	print('Database Cross References')
	print(record.dbxrefs)

	print(50 * '-')
	print('Number of features')
	print(len(record.features))

	print(50 * '-')
	print('Demonstrate usange of "in" keyword with SeqFeature objects')

	snp = 4350		# location of a Single Nucleotide Polymorphism of interest
	for feature in record.features:
		if snp in feature:
			print("%s %s" % (feature.type, feature.qualifiers.get("db_xref")))

if __name__ == '__main__':
	main()
