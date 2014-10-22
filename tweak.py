f =open('yelp_academic_dataset_tip.json')
tip=[]
for x in f:
  tip.append(json.loads(x))

f = open('yelp_academic_dataset_business.json')
business =[]
for x in f:
  business.append(json.loads(x))

f = open('yelp_academic_dataset_checkin.json')
checkin = []
for x in f:
  checkin.append(json.loads(x))

f =open('yelp_academic_dataset_user.json')
user = []
for x in f:
  user.append(json.loads(x))

f = open('yelp_academic_dataset_review.json')
review =[]
for x in f:
  review .append(json.loads(x))

# user and business attributes
view ={}
for x,i in enumerate(user):
  view[i['user_id']] = 'user[%s]'%x

for x,i in enumerate(business):
  view[i['business_id']] = 'business[%s]'%x


# user, business, review, tip, checkin

# get reviews of a particular business
k = 'dlape0CS_lVeS378Uyuoxw'
# scope for improving speed bu making separate dictionary for each business and storing reviews there
def business_reviews(k): # k is business_id
  this = []
  for i in review:
    if i['business_id'] == k:
      this.append(i)
  return this

# Restaurant on highways ; lat long--> google maps image will contain green and highways
highway=[]
for i in business:
  if 'Highway' in i['full_address']:
    highway.append(i)

#  negative reviews have more counts
## good bad count for each business
def getGoodBadCounts(k): # k is the business id
  b_r = business_reviews(k)
  count=[]
  for x,i in enumerate(b_r):
    if sentiment(i['text'])[0] <0:
      count.append(('bad', i['votes']['useful']))
    else:
      count.append(('good', i['votes']['useful']))
  return count

# image of business
def getImage(k):
  business= eval(view[k])
  lat, lon = business['latitude'], business['longitude']
  
