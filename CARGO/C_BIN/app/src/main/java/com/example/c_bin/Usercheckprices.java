package com.example.c_bin;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Usercheckprices extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    String[] pid,weight,height,distance,width,price,value;
    public static String pids,amounts;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usercheckprices);
        l1=(ListView)findViewById(R.id.lvview);
        l1.setOnItemClickListener(this);
        JsonReq JR1=new JsonReq();
        JR1.json_response=(JsonResponse)Usercheckprices.this;
        String q1="/usercheckprices";
        q1=q1.replace(" ","%20");
        JR1.execute(q1);
    }

    @Override
    public void response(JSONObject jo) {

        try {


            String status=jo.getString("status");
            Log.d("pearl",status);


            if(status.equalsIgnoreCase("success")){
                JSONArray ja1=(JSONArray)jo.getJSONArray("data");
                width=new String[ja1.length()];
                height=new String[ja1.length()];
                weight=new String[ja1.length()];
//                place=new String[ja1.length()];
                price=new String[ja1.length()];
                distance=new String[ja1.length()];
                pid=new String[ja1.length()];

                value=new String[ja1.length()];

                for(int i = 0;i<ja1.length();i++)
                {
                    pid[i]=ja1.getJSONObject(i).getString("price_id");
                    weight[i]=ja1.getJSONObject(i).getString("maximum_weight");
                    height[i]=ja1.getJSONObject(i).getString("maximum_height");
                    width[i]=ja1.getJSONObject(i).getString("maximum_width");
//                    place[i]=ja1.getJSONObject(i).getString("place");
                    distance[i]=ja1.getJSONObject(i).getString("maximum_distance");
                    price[i]=ja1.getJSONObject(i).getString("minimum_price");
                    value[i]="Weight: "+weight[i]+"\nHeight: "+height[i]+"\nWidth: "+width[i]+"\nDistance: "+distance[i]+"\nprice: "+price[i];

                }
                ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,value);
                l1.setAdapter(ar);
            }


        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        pids=pid[position];
        amounts=price[position];

        final CharSequence[] items = {"BOOK","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(Usercheckprices.this);
        // builder.setTitle("Add Photo!");
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

               if (items[item].equals("BOOK")) {

                    startActivity(new Intent(getApplicationContext(),Userbookacargo.class));
                }

                else if (items[item].equals("Cancel")) {
                    dialog.dismiss();
                }
            }

        });
        builder.show();
    }
}