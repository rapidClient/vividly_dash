from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.page import Page
from facebook_business.api import FacebookAdsApi
import time

# get campaigns
access_token = "<ACCESS_TOKEN>"
app_secret = "<APP_SECRET>"
app_id = "<APP_ID>"
id = "<AD_ACCOUNT_ID>"
FacebookAdsApi.init(access_token=access_token)

fields = [
    "name",
    "objective",
]
params = {
    "effective_status": ["ACTIVE", "PAUSED"],
}
print(
    AdAccount(id).get_campaigns(
        fields=fields,
        params=params,
    )
)

# AdInsights
fields = [
    AdsInsights.Field.impressions,
    AdsInsights.Field.inline_link_clicks,
    AdsInsights.Field.spend,
]

params = {
    "end_time": int(time.time()),
}

campaign = Campaign("<CAMPAIGN_ID>")
insights = campaign.get_insights(fields=fields, params=params)

# To get adsets
access_token = "<ACCESS_TOKEN>"
app_secret = "<APP_SECRET>"
app_id = "<APP_ID>"
id = "<AD_CAMPAIGN_ID>"
FacebookAdsApi.init(access_token=access_token)

fields = [
    "name",
    "start_time",
    "end_time",
    "daily_budget",
    "lifetime_budget",
]
params = {}
print(
    Campaign(id).get_ad_sets(
        fields=fields,
        params=params,
    )
)

# AdsInsights.Field.
# gunicorn
