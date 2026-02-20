print("Processed rows:", len(df))
print("Data processed successfully")

return df

except Exception as e:
    print("Processing error:", e)
    return None

if __name__ == "__main__":
    process_data("customers.csv")
