# This file contains functions related with Campaign
from db.mysql import connectDB, executeQuery

def createCampaign(campaign):
  """
  This saves campaign object in database and returns true if success and false if failed
  """
  conn = connectDB()
  if conn != None:
    sql = """insert into campaign (id, client_id, template_id, company_type, target_url, schedule, phone_field_name,
      mobile_field_name, billing_reference_field_name, message_content, sender_name, created_at, updated_at,
      deleted_at) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' , '{}')""" .format(campaign['id'], campaign['client_id'], campaign['template_id'], campaign['company_type'], campaign['target_url'], campaign['schedule'], campaign['phone_field_name'], campaign['mobile_field_name'], campaign['billing_reference_field_name'], campaign['message_content'], campaign['sender_name'], campaign['created_at'], campaign['updated_at'], campaign['deleted_at'])
    return executeQuery(conn, sql)
  else:
    return False



