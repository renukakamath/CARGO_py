package com.example.c_bin;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Deliveryvieworderspickedup extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {

    ListView l1;
    String[] cropname,typename,quantity,amount,date,statuss,value,oid,username,place,phone;
    public static String oids,ostatus;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_deliveryvieworderspickedup);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        l1 = (ListView) findViewById(R.id.lvview);
        l1.setOnItemClickListener(this);
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Deliveryvieworderspickedup.this;
        String q = "/deliveryboyvieworderpickup?lid="+sh.getString("log_id","");
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {

                String method = jo.getString("method");
                if (method.equalsIgnoreCase("deliveryboyupdatestatustodeliverd")) {

                    String status = jo.getString("status");
                    Log.d("pearl", status);


                    if (status.equalsIgnoreCase("success")) {
                        Toast.makeText(getApplicationContext(), "UPDATED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                        startActivity(new Intent(getApplicationContext(), Deliveryvieworderspickedup.class));

                    } else {

                        Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                    }
                } else if (method.equalsIgnoreCase("deliveryboyvieworderpickup")) {

                    String status = jo.getString("status");
                    Log.d("pearl", status);


                    if (status.equalsIgnoreCase("success")) {
                        JSONArray ja1 = (JSONArray) jo.getJSONArray("data");

                        oid = new String[ja1.length()];
                        username = new String[ja1.length()];
                        cropname = new String[ja1.length()];
                        typename = new String[ja1.length()];
                        quantity = new String[ja1.length()];
                        amount = new String[ja1.length()];
                        statuss = new String[ja1.length()];
                        phone = new String[ja1.length()];
                        value = new String[ja1.length()];

                        for (int i = 0; i < ja1.length(); i++) {

                            oid[i] = ja1.getJSONObject(i).getString("booking_id");
                            username[i] = ja1.getJSONObject(i).getString("first_name") + " " + ja1.getJSONObject(i).getString("last_name");
                            cropname[i] = ja1.getJSONObject(i).getString("weight");
                            typename[i] = ja1.getJSONObject(i).getString("width");
                            quantity[i] = ja1.getJSONObject(i).getString("from_location");
                            amount[i] = ja1.getJSONObject(i).getString("to_location");
                            statuss[i] = ja1.getJSONObject(i).getString("booking_status");
                            phone[i] = ja1.getJSONObject(i).getString("phone");
                            value[i] = "Username: " + username[i]+"\nPhone:"+phone[i] +"\nWeight: " + cropname[i] + "\nWidth: " + typename[i] + "\nFrom Location: " + quantity[i] + "\nTo Location: " + amount[i]  + "\nStatuss: " + statuss[i];

                        }
                        ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, value);
                        l1.setAdapter(ar);
                    }
                }
            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
                Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
            }
        }

        @Override
        public void onItemClick (AdapterView < ? > parent, View view,int position, long id){

            oids=oid[position];
            ostatus=statuss[position];
            final CharSequence[] items = {"Delivered","Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(Deliveryvieworderspickedup.this);
            // builder.setTitle("Add Photo!");
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                    if (items[item].equals("Delivered")) {

                        JsonReq JR = new JsonReq();
                        JR.json_response = (JsonResponse) Deliveryvieworderspickedup.this;
                        String q = "/deliveryboyupdatestatustodeliverd?oid="+Deliveryvieworderspickedup.oids+"&lid="+sh.getString("log_id","");
                        q = q.replace(" ", "%20");
                        JR.execute(q);

                    }

                    else if (items[item].equals("Cancel")) {
                        dialog.dismiss();
                    }

                }

            });
            builder.show();

    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Deliveryhome.class);
        startActivity(b);
    }
}