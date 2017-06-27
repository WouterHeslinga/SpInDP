using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using idpSpin.Models;
using Microsoft.AspNetCore.Cors;

namespace idpSpin.Controllers
{
    [EnableCors("AllowAny")]
    [Route("api")]
    public class HousesApiController : Controller
    {
        private readonly SpinContext _context;

        public HousesApiController(SpinContext context)
        {
            _context = context;
        }

        [Route("")]
        public async Task<List<Spin>> Get()
        {
            return await _context.Spin.ToListAsync();
        }

        [Route("{id}")]
        public async Task<Spin> Get(int id)
        {
            return await _context.Spin.FirstOrDefaultAsync(x => x.Id == id);
        }
        [Route("create")]
        public async Task<Spin> Post([FromBody] Spin model)
        {
            _context.Add(model);
            await _context.SaveChangesAsync();
            return model;
        }
    }
}
