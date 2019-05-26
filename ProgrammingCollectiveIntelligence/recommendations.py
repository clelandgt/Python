# -*- coding: utf-8 -*-
from math import sqrt


# set of movies
critics = {
	'Lisa Rose': {
		'Lady in the Water': 2.5,
		'Snakes on a Plane': 3.5,
		'Just My Luck': 3.0,
		'Superman Returns': 3.5,
		'You, Me and Dupree': 2.5,
		'The Night Listener': 3.0
	},
	'Gene Seymour': {
		'Lady in the Water': 3.0,
		'Snakes on a Plane': 3.5,
		'Just My Luck': 1.5,
		'Superman Returns': 5.0,
		'The Night Listener': 3.0,
		'You, Me and Dupree': 3.5
	},
	'Michael Phillips': {
		'Lady in the Water': 2.5,
		'Snakes on a Plane': 3.0,
		'Superman Returns': 3.5,
		'The Night Listener': 4.0
	},
	'Claudia Puig': {
		'Snakes on a Plane': 3.5,
		'Just My Luck': 3.0,
		'The Night Listener': 4.5,
		'Superman Returns': 4.0,
		'You, Me and Dupree': 2.5
	},
	'Mick LaSalle': {
		'Lady in the Water': 3.0,
		'Snakes on a Plane': 4.0,
		'Just My Luck': 2.0,
		'Superman Returns': 3.0,
		'The Night Listener': 3.0,
		'You, Me and Dupree': 2.0
	},
	'Jack Matthews': {
		'Lady in the Water': 3.0,
		'Snakes on a Plane': 4.0,
		'The Night Listener': 3.0,
		'Superman Returns': 5.0,
		'You, Me and Dupree': 3.5
	},
	'Toby': {
		'Snakes on a Plane': 4.5,
		'You, Me and Dupree': 1.0,
		'Superman Returns': 4.0
	}
}


def sim_distance(prefs, person1, person2):
	"""欧几里得距离评价"""
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	if len(si) == 0:
		return 0

	return 1 / (1+sum([pow(prefs[person1][item]-prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]]))


def sim_pearson(prefs, person1, person2):
	"""皮尔逊相关度评价"""
	si = []
	for item in prefs[person1]:
		if item in prefs[person2]:
			si.append(item)

	n = len(si)
	if n == 0:
		return 1

	# 所有偏好求和
	sum1 = sum([prefs[person1][item] for item in si])
	sum2 = sum([prefs[person2][item] for item in si])

	# 求平方和
	sum1Sq = sum([pow(prefs[person1][item], 2) for item in si])
	sum2Sq = sum([pow(prefs[person2][item], 2) for item in si])

	# 求乘积之和
	pSum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

	# 计算皮尔逊评价值
	num = pSum - (sum1*sum2/n)
	den = sqrt((sum1Sq-pow(sum1, 2)/n) * (sum2Sq-pow(sum2, 2)/n))
	if den == 0:
		return 0
	else:
		return num / den


def topMatches(prefs, person, n=5, similarity=sim_pearson):
	score = [(similarity(prefs, person, other), other) for other in prefs.keys() if person != other]
	score.sort()
	score.reverse()
	return score[0: n]


def main():
	print "****** sim_pearon arithmetic ******"
	print topMatches(critics, 'Toby', 5, similarity=sim_pearson)

	print "****** sim_distance arithmetic ******"
	print topMatches(critics, 'Toby', 5, similarity=sim_distance)


if __name__ == '__main__':
	main()
