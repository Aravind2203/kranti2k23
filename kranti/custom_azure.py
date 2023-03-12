from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'kranti2k23' # Must be replaced by your <storage_account_name>
    account_key = '0C6TGtGNIWFIMtobAD/YQ5TkgxrzZIz1Ev2l9lhijIsfYeejLhIFvQU816kiDQrQjOXo/8obzLYs+ASt/EGSXQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'kranti2k23' # Must be replaced by your storage_account_name
    account_key = '0C6TGtGNIWFIMtobAD/YQ5TkgxrzZIz1Ev2l9lhijIsfYeejLhIFvQU816kiDQrQjOXo/8obzLYs+ASt/EGSXQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None